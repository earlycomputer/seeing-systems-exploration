"""One conversation with one model: append-only, every call's tokens and estimated cost logged.

The three vendor adapters share one interface so the loop never branches on provider. Only the
Anthropic and Google adapters can be reached from the current cloud environment; api.openai.com is
blocked by its network policy, so the OpenAI adapter is written but has never run.

Refusal fallbacks are deliberately off: a row labelled with a model must be served by that model, and a
refusal is data. `Reply.served_model` records what actually answered.
"""

from __future__ import annotations

import base64
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path

from config import SPEND_CAP_USD, SPEND_LEDGER


@dataclass(frozen=True)
class ModelSpec:
    key: str
    label: str  # as it appears in results.md
    provider: str  # anthropic | google | openai | dry
    model_id: str
    usd_per_mtok_in: float
    usd_per_mtok_out: float
    price_source: str


MODELS = {
    "opus-5.5": ModelSpec("opus-5.5", "Opus 5.5", "anthropic", "claude-opus-5-5", 4.0, 20.0,
                          "Anthropic price table as of 2026-09-25"),
    # Second model. Id and price from third-party listings on 2026-10-03; Google's own docs are blocked
    # from the cloud box, so check https://ai.google.dev/gemini-api/docs/models before a real run.
    "gemini-3.1-pro": ModelSpec("gemini-3.1-pro", "Gemini 3.1 Pro", "google", "gemini-3.1-pro-preview", 2.0, 12.0,
                                "third-party listings, 2026-10-03, unverified"),
    # Unreachable from the cloud environment (api.openai.com denied). Same caveat on id and price.
    "gpt-5.6": ModelSpec("gpt-5.6", "GPT-5.6", "openai", "gpt-5.6-sol", 5.0, 30.0,
                         "third-party listings, 2026-10-03, unverified"),
    # Scripted stand-ins for testing the pipeline. "dry-run" always gets it right; "dry-run-echo" never does.
    "dry-run": ModelSpec("dry-run", "Dry run", "dry", "dry-run", 0.0, 0.0, "no calls are made"),
    "dry-run-echo": ModelSpec("dry-run-echo", "Dry run (echo)", "dry", "dry-run-echo", 0.0, 0.0, "no calls are made"),
}


def text(s: str) -> dict:
    return {"type": "text", "text": s}


def png(data: bytes) -> dict:
    return {"type": "png", "data": data}


@dataclass
class Reply:
    text: str
    thinking: str  # summarized reasoning where the vendor returns it; empty otherwise
    input_tokens: int
    output_tokens: int  # includes reasoning tokens
    cost_usd: float
    stop_reason: str
    served_model: str
    seconds: float
    raw: dict = field(repr=False)

    def summary(self) -> dict:
        d = {k: v for k, v in self.__dict__.items() if k != "raw"}
        return d


class BudgetExceeded(RuntimeError):
    pass


def spent_usd(ledger: Path = SPEND_LEDGER) -> float:
    if not ledger.exists():
        return 0.0
    return sum(json.loads(line)["cost_usd"] for line in ledger.read_text().splitlines() if line.strip())


def check_budget(ledger: Path = SPEND_LEDGER) -> None:
    spent = spent_usd(ledger)
    if spent >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${spent:.2f} of the ${SPEND_CAP_USD:.0f} cap; raising it needs a human first")


class Chat:
    """Base class. Subclasses implement _call(parts) -> Reply and keep their own history."""

    def __init__(self, spec: ModelSpec, system: str, effort: str = "high", ledger: Path | None = SPEND_LEDGER,
                 tag: str = ""):
        self.spec, self.system, self.effort, self.ledger, self.tag = spec, system, effort, ledger, tag

    def send(self, parts: list[dict]) -> Reply:
        if self.ledger is not None:
            check_budget(self.ledger)
        start = time.monotonic()
        reply = self._call(parts)
        reply.seconds = round(time.monotonic() - start, 2)
        if self.ledger is not None:
            self.ledger.parent.mkdir(parents=True, exist_ok=True)
            with self.ledger.open("a") as f:
                f.write(json.dumps({
                    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "model": self.spec.key,
                    "tag": self.tag, "input_tokens": reply.input_tokens, "output_tokens": reply.output_tokens,
                    "cost_usd": reply.cost_usd}) + "\n")
        return reply

    def _cost(self, tokens_in: int, tokens_out: int) -> float:
        return round(tokens_in * self.spec.usd_per_mtok_in / 1e6 + tokens_out * self.spec.usd_per_mtok_out / 1e6, 6)

    def _call(self, parts: list[dict]) -> Reply:
        raise NotImplementedError


class AnthropicChat(Chat):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        import anthropic
        self.client = anthropic.Anthropic()
        self.messages: list[dict] = []

    def _call(self, parts):
        content = []
        for p in parts:
            if p["type"] == "text":
                content.append({"type": "text", "text": p["text"]})
            else:
                content.append({"type": "image", "source": {
                    "type": "base64", "media_type": "image/png",
                    "data": base64.standard_b64encode(p["data"]).decode()}})
        self.messages.append({"role": "user", "content": content})
        with self.client.messages.stream(
            model=self.spec.model_id,
            max_tokens=32000,
            system=self.system,
            thinking={"type": "adaptive", "display": "summarized"},
            output_config={"effort": self.effort},
            messages=self.messages,
        ) as stream:
            msg = stream.get_final_message()
        # Append the full content, thinking blocks included, so the history stays valid.
        self.messages.append({"role": "assistant", "content": msg.content})
        u = msg.usage
        tokens_in = u.input_tokens + (u.cache_creation_input_tokens or 0) + (u.cache_read_input_tokens or 0)
        return Reply(
            text="".join(b.text for b in msg.content if b.type == "text"),
            thinking="\n\n".join(b.thinking for b in msg.content if b.type == "thinking" and b.thinking),
            input_tokens=tokens_in, output_tokens=u.output_tokens,
            cost_usd=self._cost(tokens_in, u.output_tokens),
            stop_reason=msg.stop_reason or "", served_model=msg.model, seconds=0.0, raw=msg.to_dict())


class GoogleChat(Chat):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        from google import genai
        from google.genai import types
        self.types = types
        self.client = genai.Client()  # GOOGLE_API_KEY or GEMINI_API_KEY
        level = {"low": "LOW", "medium": "MEDIUM"}.get(self.effort, "HIGH")
        self.chat = self.client.chats.create(model=self.spec.model_id, config=types.GenerateContentConfig(
            system_instruction=self.system, max_output_tokens=32000,
            thinking_config=types.ThinkingConfig(thinking_level=level, include_thoughts=True)))

    def _call(self, parts):
        t = self.types
        msg = [t.Part.from_text(text=p["text"]) if p["type"] == "text"
               else t.Part.from_bytes(data=p["data"], mime_type="image/png") for p in parts]
        r = self.chat.send_message(msg)
        cand = r.candidates[0] if r.candidates else None
        out_parts = (cand.content.parts if cand and cand.content and cand.content.parts else [])
        u = r.usage_metadata
        tokens_in = u.prompt_token_count or 0
        tokens_out = (u.candidates_token_count or 0) + (u.thoughts_token_count or 0)
        return Reply(
            text="".join(p.text for p in out_parts if p.text and not p.thought),
            thinking="\n\n".join(p.text for p in out_parts if p.text and p.thought),
            input_tokens=tokens_in, output_tokens=tokens_out, cost_usd=self._cost(tokens_in, tokens_out),
            stop_reason=str(cand.finish_reason) if cand else "no_candidate",
            served_model=r.model_version or self.spec.model_id, seconds=0.0,
            raw=r.model_dump(mode="json", exclude_none=True))


class OpenAIChat(Chat):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        from openai import OpenAI
        self.client = OpenAI()
        self.previous_id: str | None = None

    def _call(self, parts):
        content = [{"type": "input_text", "text": p["text"]} if p["type"] == "text" else
                   {"type": "input_image", "detail": "high",
                    "image_url": "data:image/png;base64," + base64.standard_b64encode(p["data"]).decode()}
                   for p in parts]
        r = self.client.responses.create(
            model=self.spec.model_id, instructions=self.system, input=[{"role": "user", "content": content}],
            previous_response_id=self.previous_id, reasoning={"effort": self.effort, "summary": "auto"},
            max_output_tokens=32000)
        self.previous_id = r.id
        thinking = "\n\n".join(s.text for item in r.output if item.type == "reasoning" for s in (item.summary or []))
        return Reply(
            text=r.output_text, thinking=thinking, input_tokens=r.usage.input_tokens,
            output_tokens=r.usage.output_tokens, cost_usd=self._cost(r.usage.input_tokens, r.usage.output_tokens),
            stop_reason=r.status or "", served_model=r.model, seconds=0.0, raw=r.model_dump(mode="json"))


class DryChat(Chat):
    """Plays back scripted replies. For testing the pipeline; costs nothing and writes no ledger."""

    def __init__(self, *a, script: list[str], **kw):
        super().__init__(*a, **kw)
        self.ledger = None
        self.script = list(script)

    def _call(self, parts):
        reply = self.script.pop(0)
        return Reply(text=reply, thinking="", input_tokens=0, output_tokens=0, cost_usd=0.0,
                     stop_reason="dry_run", served_model="dry-run", seconds=0.0, raw={})


KEY_VARS = {
    "anthropic": ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"),
    "google": ("GOOGLE_API_KEY", "GEMINI_API_KEY"),
    "openai": ("OPENAI_API_KEY",),
}


def open_chat(model_key: str, system: str, effort: str = "high", tag: str = "", script: list[str] | None = None,
              ledger: Path | None = SPEND_LEDGER) -> Chat:
    spec = MODELS[model_key]
    cls = {"anthropic": AnthropicChat, "google": GoogleChat, "openai": OpenAIChat, "dry": DryChat}[spec.provider]
    if cls is DryChat:
        return DryChat(spec, system, effort, None, tag, script=script or [])
    if not any(os.environ.get(v) for v in KEY_VARS[spec.provider]):
        raise SystemExit(f"{spec.label} needs one of {' or '.join(KEY_VARS[spec.provider])} in the environment")
    return cls(spec, system, effort, ledger, tag)


def extract_block(reply_text: str, lang: str) -> str | None:
    """The last fenced block of the given language, or None."""
    import re
    blocks = re.findall(rf"```{lang}\s*\n(.*?)```", reply_text, flags=re.S)
    return blocks[-1].strip() + "\n" if blocks else None
