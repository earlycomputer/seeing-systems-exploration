"""Smoke test from the handoff: load a one-body MJCF, step it 100 times, print the body position.

If this fails, fix the environment before touching anything else.
"""

import mujoco

MJCF = """
<mujoco>
  <option timestep="0.002"/>
  <worldbody>
    <body name="ball" pos="0 0 1">
      <freejoint/>
      <geom type="sphere" size="0.12"/>
    </body>
  </worldbody>
</mujoco>
"""


def main() -> None:
    model = mujoco.MjModel.from_xml_string(MJCF)
    data = mujoco.MjData(model)
    for _ in range(100):
        mujoco.mj_step(model, data)
    pos = data.body("ball").xpos
    print(f"mujoco {mujoco.__version__}  t={data.time:.3f}s  ball xpos={pos.round(4).tolist()}")
    # Free fall from 1 m for 0.2 s: z should be about 1 - 0.5 * 9.81 * 0.2**2 = 0.804.
    assert abs(pos[2] - 0.804) < 0.01, pos


if __name__ == "__main__":
    main()
