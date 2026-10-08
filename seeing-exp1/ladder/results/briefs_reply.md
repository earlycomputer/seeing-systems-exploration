```json
[
  {
    "family": "cascade",
    "versions": {
      "2": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, loose blocks are 0.12 m cubes and 0.35 kg, fixed ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts at the high end of ramp1, whose low end is 0.15 m above the floor, and rolls down to touch domino1 after a 0.10 m exit gap. Domino1 then topples across a 0.18 m center spacing and touches domino2.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"}
        ],
        "test": [
          "ball1 touches domino1",
          "domino1 touches domino2"
        ]
      },
      "4": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, loose blocks are 0.12 m cubes and 0.35 kg, fixed ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts at the high end of ramp1, whose low end is 0.15 m above the floor, and rolls down to touch domino1 after a 0.10 m exit gap. Domino1 then topples across a 0.18 m center spacing and touches domino2. Domino2 topples 0.18 m into the lower half of flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg hinged panel, making it swing clockwise through 65 degrees to its hard stop and knock cart1. Cart1 then slides 0.45 m along its horizontal slide and touches ball2, which rests at the high end of ramp2 with its low end 0.15 m above the floor.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "clockwise striking flap"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "ball2", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"}
        ],
        "test": [
          "ball1 touches domino1",
          "domino1 touches domino2",
          "flap1 swings to a stop",
          "cart1 touches ball2"
        ]
      },
      "8": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, loose blocks are 0.12 m cubes and 0.35 kg, fixed ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts at the high end of ramp1, whose low end is 0.15 m above the floor, and rolls down to touch domino1 after a 0.10 m exit gap. Domino1 then topples across a 0.18 m center spacing and touches domino2. Domino2 topples 0.18 m into the lower half of flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg hinged panel, making it swing clockwise through 65 degrees to its hard stop and knock cart1. Cart1 then slides 0.45 m along its horizontal slide and touches ball2, which rests at the high end of ramp2 with its low end 0.15 m above the floor. Ball2 rolls down ramp2 and crosses a 0.12 m gap before touching the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever carrying ball3 on its right end. Lever1 rotates clockwise through 45 degrees until its left end reaches the lower stop, and its rising right end launches ball3 vertically. Ball3 rises and then falls through ring1, centered 0.35 m below its initial center. After another 0.25 m fall, ball3 touches the bob of pendulum1, a 0.50 m long, 0.35 kg rigid pendulum hanging vertically.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "clockwise striking flap"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "ball2", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"},
          {"name": "lever1", "kind": "hinged", "what": "ball launching lever"},
          {"name": "ball3", "kind": "loose", "what": "launched falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "pendulum1", "kind": "hinged", "what": "lower impact pendulum"}
        ],
        "test": [
          "ball1 touches domino1",
          "domino1 touches domino2",
          "flap1 swings to a stop",
          "cart1 touches ball2",
          "ball2 touches lever1",
          "lever1 swings to a stop",
          "ball3 drops through ring1",
          "ball3 touches pendulum1"
        ]
      },
      "16": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, loose blocks are 0.12 m cubes and 0.35 kg, fixed ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts at the high end of ramp1, whose low end is 0.15 m above the floor, and rolls down to touch domino1 after a 0.10 m exit gap. Domino1 then topples across a 0.18 m center spacing and touches domino2. Domino2 topples 0.18 m into the lower half of flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg hinged panel, making it swing clockwise through 65 degrees to its hard stop and knock cart1. Cart1 then slides 0.45 m along its horizontal slide and touches ball2, which rests at the high end of ramp2 with its low end 0.15 m above the floor. Ball2 rolls down ramp2 and crosses a 0.12 m gap before touching the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever carrying ball3 on its right end. Lever1 rotates clockwise through 45 degrees until its left end reaches the lower stop, and its rising right end launches ball3 vertically. Ball3 rises and then falls through ring1, centered 0.35 m below its initial center. After another 0.25 m fall, ball3 touches the bob of pendulum1, a 0.50 m long, 0.35 kg rigid pendulum hanging vertically. Pendulum1 swings clockwise through 40 degrees and its bob touches domino3 after a 0.32 m arc. Domino3 topples across a 0.18 m gap into door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, making door1 swing clockwise through 70 degrees to its hard stop and knock block1. Block1 slides 0.35 m across the floor and touches cart2 on its horizontal slide. Cart2 slides 0.42 m and touches ball4 at the high end of ramp3, whose low end is 0.15 m above the floor. Ball4 rolls down ramp3 and crosses a 0.10 m gap before touching flap2, a 0.38 by 0.18 by 0.04 m, 0.28 kg hinged panel. Flap2 swings clockwise through 60 degrees to its hard stop and knocks ball5 from shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.80 m above the floor. Ball5 falls 0.30 m and drops through ring2 beneath the shelf edge. Ball5 then falls 0.35 m into bin1, whose inner footprint is 0.32 by 0.32 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "clockwise striking flap"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "ball2", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"},
          {"name": "lever1", "kind": "hinged", "what": "ball launching lever"},
          {"name": "ball3", "kind": "loose", "what": "first falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "pendulum1", "kind": "hinged", "what": "impact pendulum"},
          {"name": "domino3", "kind": "loose", "what": "third upright domino"},
          {"name": "door1", "kind": "hinged", "what": "clockwise hinged door"},
          {"name": "block1", "kind": "loose", "what": "door struck block"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"},
          {"name": "ball4", "kind": "loose", "what": "third ramp ball"},
          {"name": "ramp3", "kind": "fixed", "what": "third inclined ramp"},
          {"name": "flap2", "kind": "hinged", "what": "second striking flap"},
          {"name": "ball5", "kind": "loose", "what": "final falling ball"},
          {"name": "shelf1", "kind": "fixed", "what": "ball support shelf"},
          {"name": "ring2", "kind": "fixed", "what": "second horizontal ring"},
          {"name": "bin1", "kind": "fixed", "what": "final catch bin"}
        ],
        "test": [
          "ball1 touches domino1",
          "domino1 touches domino2",
          "flap1 swings to a stop",
          "cart1 touches ball2",
          "ball2 touches lever1",
          "lever1 swings to a stop",
          "ball3 drops through ring1",
          "ball3 touches pendulum1",
          "pendulum1 touches domino3",
          "door1 swings to a stop",
          "block1 touches cart2",
          "cart2 touches ball4",
          "ball4 touches flap2",
          "flap2 swings to a stop",
          "ball5 drops through ring2",
          "ball5 comes to rest in bin1"
        ]
      }
    }
  },
  {
    "family": "orbit",
    "versions": {
      "2": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 0.95 m long and 0.30 m wide at 19 degrees, and horizontal rings have 0.16 m clear diameter. Pendulum1 is a 0.55 m long, 0.40 kg rigid pendulum released 55 degrees left of vertical, and it swings clockwise to touch ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.12 m gap, and touches cart1.",
        "things": [
          {"name": "pendulum1", "kind": "hinged", "what": "starting pendulum"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"}
        ],
        "test": [
          "pendulum1 touches ball1",
          "ball1 touches cart1"
        ]
      },
      "4": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 0.95 m long and 0.30 m wide at 19 degrees, and horizontal rings have 0.16 m clear diameter. Pendulum1 is a 0.55 m long, 0.40 kg rigid pendulum released 55 degrees left of vertical, and it swings clockwise to touch ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.12 m gap, and touches cart1. Cart1 slides 0.40 m along its horizontal slide and touches domino1. Domino1 topples 0.18 m into flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg panel, making flap1 swing clockwise through 65 degrees to its hard stop and knock ball2 at the high end of ramp2.",
        "things": [
          {"name": "pendulum1", "kind": "hinged", "what": "starting pendulum"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "first striking flap"},
          {"name": "ball2", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"}
        ],
        "test": [
          "pendulum1 touches ball1",
          "ball1 touches cart1",
          "cart1 touches domino1",
          "flap1 swings to a stop"
        ]
      },
      "8": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 0.95 m long and 0.30 m wide at 19 degrees, and horizontal rings have 0.16 m clear diameter. Pendulum1 is a 0.55 m long, 0.40 kg rigid pendulum released 55 degrees left of vertical, and it swings clockwise to touch ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.12 m gap, and touches cart1. Cart1 slides 0.40 m along its horizontal slide and touches domino1. Domino1 topples 0.18 m into flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg panel, making flap1 swing clockwise through 65 degrees to its hard stop and knock ball2 at the high end of ramp2. Ball2 rolls down ramp2, whose low end is 0.15 m above the floor, and touches the left end of seesaw1 after a 0.10 m exit gap. Seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying block1 on its right end, rotates clockwise through 40 degrees to its stop and launches block1 upward. Block1 rises and then drops through ring1, centered 0.30 m below its initial center. Block1 falls another 0.25 m and touches door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg hinged panel.",
        "things": [
          {"name": "pendulum1", "kind": "hinged", "what": "starting pendulum"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "first striking flap"},
          {"name": "ball2", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"},
          {"name": "seesaw1", "kind": "hinged", "what": "block launching seesaw"},
          {"name": "block1", "kind": "loose", "what": "launched falling block"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "door1", "kind": "hinged", "what": "block struck door"}
        ],
        "test": [
          "pendulum1 touches ball1",
          "ball1 touches cart1",
          "cart1 touches domino1",
          "flap1 swings to a stop",
          "ball2 touches seesaw1",
          "seesaw1 swings to a stop",
          "block1 drops through ring1",
          "block1 touches door1"
        ]
      },
      "16": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 0.95 m long and 0.30 m wide at 19 degrees, and horizontal rings have 0.16 m clear diameter. Pendulum1 is a 0.55 m long, 0.40 kg rigid pendulum released 55 degrees left of vertical, and it swings clockwise to touch ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.12 m gap, and touches cart1. Cart1 slides 0.40 m along its horizontal slide and touches domino1. Domino1 topples 0.18 m into flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg panel, making flap1 swing clockwise through 65 degrees to its hard stop and knock ball2 at the high end of ramp2. Ball2 rolls down ramp2, whose low end is 0.15 m above the floor, and touches the left end of seesaw1 after a 0.10 m exit gap. Seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying block1 on its right end, rotates clockwise through 40 degrees to its stop and launches block1 upward. Block1 rises and then drops through ring1, centered 0.30 m below its initial center. Block1 falls another 0.25 m and touches door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg hinged panel. Door1 swings clockwise through 70 degrees to its hard stop and knocks cart2. Cart2 slides 0.42 m and touches the bob of pendulum2, a 0.50 m long, 0.35 kg pendulum hanging vertically. Pendulum2 swings clockwise through 38 degrees and touches ball3 at the high end of ramp3. Ball3 rolls down ramp3, whose low end is 0.15 m above the floor, and touches domino2 after a 0.10 m exit gap. Domino2 topples across a 0.18 m gap and touches flap2, a 0.38 by 0.18 by 0.04 m, 0.28 kg hinged panel. Flap2 swings clockwise through 60 degrees to its hard stop and knocks ball4 from shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.78 m above the floor. Ball4 falls 0.30 m and drops through ring2 beneath the shelf edge. Ball4 falls another 0.35 m into box1, whose inner footprint is 0.32 by 0.32 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.",
        "things": [
          {"name": "pendulum1", "kind": "hinged", "what": "starting pendulum"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "first striking flap"},
          {"name": "ball2", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"},
          {"name": "seesaw1", "kind": "hinged", "what": "block launching seesaw"},
          {"name": "block1", "kind": "loose", "what": "launched falling block"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "door1", "kind": "hinged", "what": "clockwise hinged door"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"},
          {"name": "pendulum2", "kind": "hinged", "what": "second pendulum"},
          {"name": "ball3", "kind": "loose", "what": "third ramp ball"},
          {"name": "ramp3", "kind": "fixed", "what": "third inclined ramp"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "flap2", "kind": "hinged", "what": "second striking flap"},
          {"name": "ball4", "kind": "loose", "what": "final falling ball"},
          {"name": "shelf1", "kind": "fixed", "what": "ball support shelf"},
          {"name": "ring2", "kind": "fixed", "what": "second horizontal ring"},
          {"name": "box1", "kind": "fixed", "what": "final catch box"}
        ],
        "test": [
          "pendulum1 touches ball1",
          "ball1 touches cart1",
          "cart1 touches domino1",
          "flap1 swings to a stop",
          "ball2 touches seesaw1",
          "seesaw1 swings to a stop",
          "block1 drops through ring1",
          "block1 touches door1",
          "door1 swings to a stop",
          "cart2 touches pendulum2",
          "pendulum2 touches ball3",
          "ball3 touches domino2",
          "domino2 touches flap2",
          "flap2 swings to a stop",
          "ball4 drops through ring2",
          "ball4 comes to rest in box1"
        ]
      }
    }
  },
  {
    "family": "zigzag",
    "versions": {
      "2": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.72, restitution 0.04, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts 0.30 m above ring1 and drops vertically through it. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "lever1", "kind": "hinged", "what": "cart striking lever"}
        ],
        "test": [
          "ball1 drops through ring1",
          "ball1 touches lever1"
        ]
      },
      "4": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.72, restitution 0.04, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts 0.30 m above ring1 and drops vertically through it. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its lower stop, and its rising right end knocks cart1 along a horizontal slide. Cart1 slides 0.42 m and touches domino1.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "lever1", "kind": "hinged", "what": "cart striking lever"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"}
        ],
        "test": [
          "ball1 drops through ring1",
          "ball1 touches lever1",
          "lever1 swings to a stop",
          "cart1 touches domino1"
        ]
      },
      "8": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.72, restitution 0.04, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts 0.30 m above ring1 and drops vertically through it. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its lower stop, and its rising right end knocks cart1 along a horizontal slide. Cart1 slides 0.42 m and touches domino1. Domino1 topples across a 0.18 m spacing and touches ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and strikes pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches block1.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "lever1", "kind": "hinged", "what": "cart striking lever"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "ball2", "kind": "loose", "what": "ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "inclined ramp"},
          {"name": "door1", "kind": "hinged", "what": "pendulum striking door"},
          {"name": "pendulum1", "kind": "hinged", "what": "block striking pendulum"},
          {"name": "block1", "kind": "loose", "what": "pendulum struck block"}
        ],
        "test": [
          "ball1 drops through ring1",
          "ball1 touches lever1",
          "lever1 swings to a stop",
          "cart1 touches domino1",
          "domino1 touches ball2",
          "ball2 touches door1",
          "door1 swings to a stop",
          "pendulum1 touches block1"
        ]
      },
      "16": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.72, restitution 0.04, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts 0.30 m above ring1 and drops vertically through it. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its lower stop, and its rising right end knocks cart1 along a horizontal slide. Cart1 slides 0.42 m and touches domino1. Domino1 topples across a 0.18 m spacing and touches ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and strikes pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches block1. Block1 slides 0.35 m across the floor and touches cart2. Cart2 slides 0.42 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying ball3 on its right end. Seesaw1 rotates clockwise through 42 degrees to its lower stop and launches ball3 vertically from its rising right end. Ball3 rises and then drops through ring2, centered 0.32 m below its initial center. Ball3 falls another 0.24 m and touches domino2. Domino2 topples across a 0.18 m gap and touches flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg hinged panel. Flap1 swings clockwise through 60 degrees to its hard stop and knocks ball4 from shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.55 m above cup1. Ball4 falls into cup1, whose inner footprint is 0.30 by 0.30 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.",
        "things": [
          {"name": "ball1", "kind": "loose", "what": "starting falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "lever1", "kind": "hinged", "what": "cart striking lever"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "ball2", "kind": "loose", "what": "ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "inclined ramp"},
          {"name": "door1", "kind": "hinged", "what": "pendulum striking door"},
          {"name": "pendulum1", "kind": "hinged", "what": "block striking pendulum"},
          {"name": "block1", "kind": "loose", "what": "pendulum struck block"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"},
          {"name": "seesaw1", "kind": "hinged", "what": "ball launching seesaw"},
          {"name": "ball3", "kind": "loose", "what": "launched falling ball"},
          {"name": "ring2", "kind": "fixed", "what": "second horizontal ring"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "flap1", "kind": "hinged", "what": "final striking flap"},
          {"name": "ball4", "kind": "loose", "what": "final catch ball"},
          {"name": "shelf1", "kind": "fixed", "what": "ball support shelf"},
          {"name": "cup1", "kind": "fixed", "what": "final catch cup"}
        ],
        "test": [
          "ball1 drops through ring1",
          "ball1 touches lever1",
          "lever1 swings to a stop",
          "cart1 touches domino1",
          "domino1 touches ball2",
          "ball2 touches door1",
          "door1 swings to a stop",
          "pendulum1 touches block1",
          "block1 touches cart2",
          "cart2 touches seesaw1",
          "seesaw1 swings to a stop",
          "ball3 drops through ring2",
          "ball3 touches domino2",
          "domino2 touches flap1",
          "flap1 swings to a stop",
          "ball4 comes to rest in cup1"
        ]
      }
    }
  },
  {
    "family": "spring",
    "versions": {
      "2": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Cart1 starts with its axial slide spring compressed 0.20 m; the spring stiffness is 18 N/m, and cart1 travels 0.50 m before touching ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches the bob of pendulum1.",
        "things": [
          {"name": "cart1", "kind": "sliding", "what": "spring driven cart"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "pendulum1", "kind": "hinged", "what": "first pendulum"}
        ],
        "test": [
          "cart1 touches ball1",
          "ball1 touches pendulum1"
        ]
      },
      "4": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Cart1 starts with its axial slide spring compressed 0.20 m; the spring stiffness is 18 N/m, and cart1 travels 0.50 m before touching ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches the bob of pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 40 degrees and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and knocks block1.",
        "things": [
          {"name": "cart1", "kind": "sliding", "what": "spring driven cart"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "pendulum1", "kind": "hinged", "what": "first pendulum"},
          {"name": "door1", "kind": "hinged", "what": "block striking door"},
          {"name": "block1", "kind": "loose", "what": "door struck block"}
        ],
        "test": [
          "cart1 touches ball1",
          "ball1 touches pendulum1",
          "pendulum1 touches door1",
          "door1 swings to a stop"
        ]
      },
      "8": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Cart1 starts with its axial slide spring compressed 0.20 m; the spring stiffness is 18 N/m, and cart1 travels 0.50 m before touching ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches the bob of pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 40 degrees and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and knocks block1. Block1 slides 0.32 m across the floor and touches domino1. Domino1 topples 0.18 m into the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever carrying ball2 on its right end; lever1 rotates clockwise through 45 degrees to its stop and launches ball2. Ball2 rises and then drops through ring1, centered 0.32 m below its initial center. Ball2 falls another 0.25 m and touches cart2.",
        "things": [
          {"name": "cart1", "kind": "sliding", "what": "spring driven cart"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "pendulum1", "kind": "hinged", "what": "first pendulum"},
          {"name": "door1", "kind": "hinged", "what": "block striking door"},
          {"name": "block1", "kind": "loose", "what": "door struck block"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "lever1", "kind": "hinged", "what": "ball launching lever"},
          {"name": "ball2", "kind": "loose", "what": "first falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"}
        ],
        "test": [
          "cart1 touches ball1",
          "ball1 touches pendulum1",
          "pendulum1 touches door1",
          "door1 swings to a stop",
          "block1 touches domino1",
          "lever1 swings to a stop",
          "ball2 drops through ring1",
          "ball2 touches cart2"
        ]
      },
      "16": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Cart1 starts with its axial slide spring compressed 0.20 m; the spring stiffness is 18 N/m, and cart1 travels 0.50 m before touching ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches the bob of pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 40 degrees and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and knocks block1. Block1 slides 0.32 m across the floor and touches domino1. Domino1 topples 0.18 m into the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever carrying ball2 on its right end; lever1 rotates clockwise through 45 degrees to its stop and launches ball2. Ball2 rises and then drops through ring1, centered 0.32 m below its initial center. Ball2 falls another 0.25 m and touches cart2. Cart2 slides 0.40 m and touches domino2. Domino2 topples across a 0.18 m spacing and touches ball3 at the high end of ramp2. Ball3 rolls down ramp2, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches flap1. Flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg panel, swings clockwise through 60 degrees to its hard stop and strikes pendulum2. Pendulum2, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches ball4 on shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.85 m above the floor. Ball4 falls 0.30 m and drops through ring2 beneath the shelf edge. Ball4 falls another 0.25 m and touches the left end of seesaw1. Seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying ball5 on its right end, rotates clockwise through 42 degrees to its hard stop and launches ball5 upward.",
        "things": [
          {"name": "cart1", "kind": "sliding", "what": "spring driven cart"},
          {"name": "ball1", "kind": "loose", "what": "first ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "first inclined ramp"},
          {"name": "pendulum1", "kind": "hinged", "what": "first pendulum"},
          {"name": "door1", "kind": "hinged", "what": "block striking door"},
          {"name": "block1", "kind": "loose", "what": "door struck block"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "lever1", "kind": "hinged", "what": "ball launching lever"},
          {"name": "ball2", "kind": "loose", "what": "first falling ball"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "ball3", "kind": "loose", "what": "second ramp ball"},
          {"name": "ramp2", "kind": "fixed", "what": "second inclined ramp"},
          {"name": "flap1", "kind": "hinged", "what": "pendulum striking flap"},
          {"name": "pendulum2", "kind": "hinged", "what": "second pendulum"},
          {"name": "ball4", "kind": "loose", "what": "second falling ball"},
          {"name": "shelf1", "kind": "fixed", "what": "ball support shelf"},
          {"name": "ring2", "kind": "fixed", "what": "second horizontal ring"},
          {"name": "seesaw1", "kind": "hinged", "what": "final launching seesaw"},
          {"name": "ball5", "kind": "loose", "what": "final launched ball"}
        ],
        "test": [
          "cart1 touches ball1",
          "ball1 touches pendulum1",
          "pendulum1 touches door1",
          "door1 swings to a stop",
          "block1 touches domino1",
          "lever1 swings to a stop",
          "ball2 drops through ring1",
          "ball2 touches cart2",
          "cart2 touches domino2",
          "domino2 touches ball3",
          "ball3 touches flap1",
          "flap1 swings to a stop",
          "pendulum2 touches ball4",
          "ball4 drops through ring2",
          "ball4 touches seesaw1",
          "seesaw1 swings to a stop"
        ]
      }
    }
  },
  {
    "family": "ascent",
    "versions": {
      "2": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Block1 starts 0.30 m above ring1 and drops vertically through it. Block1 falls another 0.25 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam.",
        "things": [
          {"name": "block1", "kind": "loose", "what": "starting falling block"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "seesaw1", "kind": "hinged", "what": "first launching seesaw"}
        ],
        "test": [
          "block1 drops through ring1",
          "block1 touches seesaw1"
        ]
      },
      "4": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Block1 starts 0.30 m above ring1 and drops vertically through it. Block1 falls another 0.25 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam. Seesaw1 rotates clockwise through 42 degrees to its lower stop and launches ball1 from its rising right end. Ball1 travels 0.45 m through the air and touches domino1.",
        "things": [
          {"name": "block1", "kind": "loose", "what": "starting falling block"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "seesaw1", "kind": "hinged", "what": "first launching seesaw"},
          {"name": "ball1", "kind": "loose", "what": "first launched ball"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"}
        ],
        "test": [
          "block1 drops through ring1",
          "block1 touches seesaw1",
          "seesaw1 swings to a stop",
          "ball1 touches domino1"
        ]
      },
      "8": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Block1 starts 0.30 m above ring1 and drops vertically through it. Block1 falls another 0.25 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam. Seesaw1 rotates clockwise through 42 degrees to its lower stop and launches ball1 from its rising right end. Ball1 travels 0.45 m through the air and touches domino1. Domino1 topples across a 0.18 m spacing and touches cart1. Cart1 slides 0.40 m and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and knocks ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches pendulum1.",
        "things": [
          {"name": "block1", "kind": "loose", "what": "starting falling block"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "seesaw1", "kind": "hinged", "what": "first launching seesaw"},
          {"name": "ball1", "kind": "loose", "what": "first launched ball"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "door1", "kind": "hinged", "what": "ramp ball striking door"},
          {"name": "ball2", "kind": "loose", "what": "ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "inclined ramp"},
          {"name": "pendulum1", "kind": "hinged", "what": "impact pendulum"}
        ],
        "test": [
          "block1 drops through ring1",
          "block1 touches seesaw1",
          "seesaw1 swings to a stop",
          "ball1 touches domino1",
          "domino1 touches cart1",
          "cart1 touches door1",
          "door1 swings to a stop",
          "ball2 touches pendulum1"
        ]
      },
      "16": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Block1 starts 0.30 m above ring1 and drops vertically through it. Block1 falls another 0.25 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam. Seesaw1 rotates clockwise through 42 degrees to its lower stop and launches ball1 from its rising right end. Ball1 travels 0.45 m through the air and touches domino1. Domino1 topples across a 0.18 m spacing and touches cart1. Cart1 slides 0.40 m and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and knocks ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches flap1. Flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg panel, swings clockwise through 60 degrees to its hard stop and knocks block2. Block2 slides 0.34 m across the floor and touches domino2. Domino2 topples across a 0.18 m spacing and touches cart2. Cart2 slides 0.42 m and touches the left end of lever2, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever carrying ball3 on its right end. Lever2 rotates clockwise through 45 degrees to its hard stop and launches ball3 vertically. Ball3 rises and then drops through ring2, centered 0.32 m below its initial center. Ball3 falls another 0.35 m into box1, whose inner footprint is 0.32 by 0.32 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.",
        "things": [
          {"name": "block1", "kind": "loose", "what": "starting falling block"},
          {"name": "ring1", "kind": "fixed", "what": "first horizontal ring"},
          {"name": "seesaw1", "kind": "hinged", "what": "first launching seesaw"},
          {"name": "ball1", "kind": "loose", "what": "first launched ball"},
          {"name": "domino1", "kind": "loose", "what": "first upright domino"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "door1", "kind": "hinged", "what": "ramp ball striking door"},
          {"name": "ball2", "kind": "loose", "what": "ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "inclined ramp"},
          {"name": "pendulum1", "kind": "hinged", "what": "impact pendulum"},
          {"name": "flap1", "kind": "hinged", "what": "block striking flap"},
          {"name": "block2", "kind": "loose", "what": "flap struck block"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"},
          {"name": "lever2", "kind": "hinged", "what": "final launching lever"},
          {"name": "ball3", "kind": "loose", "what": "final falling ball"},
          {"name": "ring2", "kind": "fixed", "what": "second horizontal ring"},
          {"name": "box1", "kind": "fixed", "what": "final catch box"}
        ],
        "test": [
          "block1 drops through ring1",
          "block1 touches seesaw1",
          "seesaw1 swings to a stop",
          "ball1 touches domino1",
          "domino1 touches cart1",
          "cart1 touches door1",
          "door1 swings to a stop",
          "ball2 touches pendulum1",
          "pendulum1 touches flap1",
          "flap1 swings to a stop",
          "block2 touches domino2",
          "domino2 touches cart2",
          "cart2 touches lever2",
          "lever2 swings to a stop",
          "ball3 drops through ring2",
          "ball3 comes to rest in box1"
        ]
      }
    }
  },
  {
    "family": "spiral",
    "versions": {
      "2": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal hoops or rings have 0.16 m clear diameter. Domino1 starts tilted 8 degrees toward domino2 and topples across their 0.18 m center spacing to touch domino2. Domino2 then topples across a 0.18 m gap and touches cart1.",
        "things": [
          {"name": "domino1", "kind": "loose", "what": "starting tilted domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"}
        ],
        "test": [
          "domino1 touches domino2",
          "domino2 touches cart1"
        ]
      },
      "4": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal hoops or rings have 0.16 m clear diameter. Domino1 starts tilted 8 degrees toward domino2 and topples across their 0.18 m center spacing to touch domino2. Domino2 then topples across a 0.18 m gap and touches cart1. Cart1 slides 0.40 m on platform1, a fixed 0.80 by 0.35 by 0.05 m platform 0.90 m above the floor, and touches ball1 at its edge. Ball1 falls 0.30 m and drops through hoop1 below the platform edge.",
        "things": [
          {"name": "domino1", "kind": "loose", "what": "starting tilted domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "platform1", "kind": "fixed", "what": "first elevated platform"},
          {"name": "ball1", "kind": "loose", "what": "first falling ball"},
          {"name": "hoop1", "kind": "fixed", "what": "first horizontal hoop"}
        ],
        "test": [
          "domino1 touches domino2",
          "domino2 touches cart1",
          "cart1 touches ball1",
          "ball1 drops through hoop1"
        ]
      },
      "8": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal hoops or rings have 0.16 m clear diameter. Domino1 starts tilted 8 degrees toward domino2 and topples across their 0.18 m center spacing to touch domino2. Domino2 then topples across a 0.18 m gap and touches cart1. Cart1 slides 0.40 m on platform1, a fixed 0.80 by 0.35 by 0.05 m platform 0.90 m above the floor, and touches ball1 at its edge. Ball1 falls 0.30 m and drops through hoop1 below the platform edge. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its hard stop and its rising right end strikes pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches flap1. Flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg panel, swings clockwise through 60 degrees to its hard stop and knocks ball2 at the high end of ramp1.",
        "things": [
          {"name": "domino1", "kind": "loose", "what": "starting tilted domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "platform1", "kind": "fixed", "what": "first elevated platform"},
          {"name": "ball1", "kind": "loose", "what": "first falling ball"},
          {"name": "hoop1", "kind": "fixed", "what": "first horizontal hoop"},
          {"name": "lever1", "kind": "hinged", "what": "pendulum striking lever"},
          {"name": "pendulum1", "kind": "hinged", "what": "flap striking pendulum"},
          {"name": "flap1", "kind": "hinged", "what": "ramp ball striking flap"},
          {"name": "ball2", "kind": "loose", "what": "ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "inclined ramp"}
        ],
        "test": [
          "domino1 touches domino2",
          "domino2 touches cart1",
          "cart1 touches ball1",
          "ball1 drops through hoop1",
          "ball1 touches lever1",
          "lever1 swings to a stop",
          "pendulum1 touches flap1",
          "flap1 swings to a stop"
        ]
      },
      "16": {
        "brief": "Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, blocks are 0.12 m cubes and 0.35 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal hoops or rings have 0.16 m clear diameter. Domino1 starts tilted 8 degrees toward domino2 and topples across their 0.18 m center spacing to touch domino2. Domino2 then topples across a 0.18 m gap and touches cart1. Cart1 slides 0.40 m on platform1, a fixed 0.80 by 0.35 by 0.05 m platform 0.90 m above the floor, and touches ball1 at its edge. Ball1 falls 0.30 m and drops through hoop1 below the platform edge. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its hard stop and its rising right end strikes pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches flap1. Flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg panel, swings clockwise through 60 degrees to its hard stop and knocks ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches domino3. Domino3 topples across a 0.18 m gap into door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, making door1 swing clockwise through 70 degrees to its hard stop and knock cart2. Cart2 slides 0.42 m across platform2, a fixed 0.80 by 0.35 by 0.05 m platform 0.85 m above the floor, and touches block1 at its edge. Block1 falls 0.30 m and drops through ring2 below the platform edge. Block1 falls another 0.25 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying ball3 on its right end. Seesaw1 rotates clockwise through 42 degrees to its hard stop and launches ball3 vertically. Ball3 rises and then drops through ring3, centered 0.32 m below its initial center. Ball3 falls another 0.35 m into cup1, whose inner footprint is 0.30 by 0.30 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.",
        "things": [
          {"name": "domino1", "kind": "loose", "what": "starting tilted domino"},
          {"name": "domino2", "kind": "loose", "what": "second upright domino"},
          {"name": "cart1", "kind": "sliding", "what": "first slide cart"},
          {"name": "platform1", "kind": "fixed", "what": "first elevated platform"},
          {"name": "ball1", "kind": "loose", "what": "first falling ball"},
          {"name": "hoop1", "kind": "fixed", "what": "first horizontal hoop"},
          {"name": "lever1", "kind": "hinged", "what": "pendulum striking lever"},
          {"name": "pendulum1", "kind": "hinged", "what": "flap striking pendulum"},
          {"name": "flap1", "kind": "hinged", "what": "ramp ball striking flap"},
          {"name": "ball2", "kind": "loose", "what": "ramp ball"},
          {"name": "ramp1", "kind": "fixed", "what": "inclined ramp"},
          {"name": "domino3", "kind": "loose", "what": "third upright domino"},
          {"name": "door1", "kind": "hinged", "what": "cart striking door"},
          {"name": "cart2", "kind": "sliding", "what": "second slide cart"},
          {"name": "platform2", "kind": "fixed", "what": "second elevated platform"},
          {"name": "block1", "kind": "loose", "what": "second falling body"},
          {"name": "ring2", "kind": "fixed", "what": "second horizontal ring"},
          {"name": "seesaw1", "kind": "hinged", "what": "final launching seesaw"},
          {"name": "ball3", "kind": "loose", "what": "final falling ball"},
          {"name": "ring3", "kind": "fixed", "what": "third horizontal ring"},
          {"name": "cup1", "kind": "fixed", "what": "final catch cup"}
        ],
        "test": [
          "domino1 touches domino2",
          "domino2 touches cart1",
          "cart1 touches ball1",
          "ball1 drops through hoop1",
          "ball1 touches lever1",
          "lever1 swings to a stop",
          "pendulum1 touches flap1",
          "flap1 swings to a stop",
          "ball2 touches domino3",
          "door1 swings to a stop",
          "cart2 touches block1",
          "block1 drops through ring2",
          "block1 touches seesaw1",
          "seesaw1 swings to a stop",
          "ball3 drops through ring3",
          "ball3 comes to rest in cup1"
        ]
      }
    }
  }
]
```