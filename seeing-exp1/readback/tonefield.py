"""512 render -> tone field: box-filter downsample to a small grayscale image (handoff, step 3)."""

from __future__ import annotations

import numpy as np

from config import RENDER_SIZE


def tone_field(img: np.ndarray, res: int) -> np.ndarray:
    k = RENDER_SIZE // res
    assert img.shape == (RENDER_SIZE, RENDER_SIZE) and k * res == RENDER_SIZE
    return img.reshape(res, k, res, k).mean(axis=(1, 3))


def preview(tone: np.ndarray) -> np.ndarray:
    """Nearest-neighbour upscale back to 512 so a person can see what the model was sent. Never sent."""
    k = RENDER_SIZE // tone.shape[0]
    return np.kron(tone, np.ones((k, k)))
