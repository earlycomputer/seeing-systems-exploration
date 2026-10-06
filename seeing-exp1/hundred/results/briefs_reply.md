```json
[
  {
    "id": "domino",
    "brief": "ball1 starts 1 m up ramp and rolls into d1, which topples d2, then d3, and d3 knocks ball2 into cup where it rests.",
    "things": [
      {"name": "ball1", "kind": "loose", "what": "trigger ball"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "d1", "kind": "loose", "what": "first domino"},
      {"name": "d2", "kind": "loose", "what": "second domino"},
      {"name": "d3", "kind": "loose", "what": "third domino"},
      {"name": "ball2", "kind": "loose", "what": "target ball"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "ball1 touches d1",
      "d1 touches d2",
      "d2 touches d3",
      "d3 touches ball2",
      "ball2 comes to rest in cup"
    ]
  },
  {
    "id": "catapult",
    "brief": "pendulum released from 0.6 m above its lowest point strikes cart, which knocks weight onto one end of seesaw so seesaw reaches its lower stop and throws ball into cup where it rests.",
    "things": [
      {"name": "pendulum", "kind": "hinged", "what": "swinging striker"},
      {"name": "cart", "kind": "sliding", "what": "impact cart"},
      {"name": "weight", "kind": "loose", "what": "falling seesaw weight"},
      {"name": "seesaw", "kind": "hinged", "what": "launching lever"},
      {"name": "ball", "kind": "loose", "what": "launched ball"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "pendulum touches cart",
      "cart touches weight",
      "weight touches seesaw",
      "seesaw reaches its lower stop",
      "ball comes to rest in cup"
    ]
  },
  {
    "id": "trapdoors",
    "brief": "ball1 begins 0.8 m above hoop1 and drops through it onto flap1, whose swing to its lower stop releases block to strike flap2; flap2 reaches its lower stop and releases ball2 through hoop2 into cup where it rests.",
    "things": [
      {"name": "ball1", "kind": "loose", "what": "first falling ball"},
      {"name": "hoop1", "kind": "fixed", "what": "first drop hoop"},
      {"name": "flap1", "kind": "hinged", "what": "first trapdoor"},
      {"name": "block", "kind": "loose", "what": "released striker"},
      {"name": "flap2", "kind": "hinged", "what": "second trapdoor"},
      {"name": "ball2", "kind": "loose", "what": "final falling ball"},
      {"name": "hoop2", "kind": "fixed", "what": "second drop hoop"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "ball1 drops through hoop1",
      "flap1 reaches its lower stop",
      "block touches flap2",
      "flap2 reaches its lower stop",
      "ball2 drops through hoop2",
      "ball2 comes to rest in cup"
    ]
  },
  {
    "id": "newton",
    "brief": "pendulum released from 0.5 m above its lowest point strikes four equal balls spaced 0.15 m apart along rail, passing the impacts from ball1 through ball4 so ball4 enters box and rests.",
    "things": [
      {"name": "pendulum", "kind": "hinged", "what": "initial striker"},
      {"name": "ball1", "kind": "loose", "what": "first impact ball"},
      {"name": "ball2", "kind": "loose", "what": "second impact ball"},
      {"name": "ball3", "kind": "loose", "what": "third impact ball"},
      {"name": "ball4", "kind": "loose", "what": "final impact ball"},
      {"name": "rail", "kind": "fixed", "what": "level guide"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "pendulum touches ball1",
      "ball1 touches ball2",
      "ball2 touches ball3",
      "ball3 touches ball4",
      "ball4 comes to rest in box"
    ]
  },
  {
    "id": "gate",
    "brief": "ball starts 1 m up ramp and rolls into paddle, which swings into slider; slider knocks block off ledge so block drops through hoop into box and rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "trigger ball"},
      {"name": "ramp", "kind": "fixed", "what": "ball ramp"},
      {"name": "paddle", "kind": "hinged", "what": "swinging gate"},
      {"name": "slider", "kind": "sliding", "what": "horizontal striker"},
      {"name": "block", "kind": "loose", "what": "falling payload"},
      {"name": "ledge", "kind": "fixed", "what": "payload ledge"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "ball touches paddle",
      "paddle touches slider",
      "slider touches block",
      "block drops through hoop",
      "block comes to rest in box"
    ]
  },
  {
    "id": "rebound",
    "brief": "block falls 0.5 m onto spring-loaded plunger, whose rebound makes it strike ball up ramp so ball descends through hoop into cup and rests.",
    "things": [
      {"name": "block", "kind": "loose", "what": "falling compressor"},
      {"name": "plunger", "kind": "sliding", "what": "spring-loaded striker"},
      {"name": "ball", "kind": "loose", "what": "launched ball"},
      {"name": "ramp", "kind": "fixed", "what": "launch ramp"},
      {"name": "hoop", "kind": "fixed", "what": "flight hoop"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "block touches plunger",
      "plunger touches ball",
      "ball drops through hoop",
      "ball comes to rest in cup"
    ]
  },
  {
    "id": "railcart",
    "brief": "cart descends 1.2 m along rail and hits domino, which falls against flap; flap reaches its lower stop and releases ball through ring into box where it rests.",
    "things": [
      {"name": "cart", "kind": "sliding", "what": "descending cart"},
      {"name": "rail", "kind": "fixed", "what": "inclined cart rail"},
      {"name": "domino", "kind": "loose", "what": "flap striker"},
      {"name": "flap", "kind": "hinged", "what": "release flap"},
      {"name": "ball", "kind": "loose", "what": "released ball"},
      {"name": "ring", "kind": "fixed", "what": "drop opening"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "cart touches domino",
      "domino touches flap",
      "flap reaches its lower stop",
      "ball drops through ring",
      "ball comes to rest in box"
    ]
  },
  {
    "id": "tiptray",
    "brief": "weight drops 0.6 m into tray, tipping tray to its lower stop so ball1 rolls out into ball2; ball2 knocks block through hoop and into bin where it rests.",
    "things": [
      {"name": "weight", "kind": "loose", "what": "tray tipping weight"},
      {"name": "tray", "kind": "hinged", "what": "tipping tray"},
      {"name": "ball1", "kind": "loose", "what": "spilled ball"},
      {"name": "ball2", "kind": "loose", "what": "transfer ball"},
      {"name": "block", "kind": "loose", "what": "final payload"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "bin", "kind": "fixed", "what": "catching bin"}
    ],
    "test": [
      "weight touches tray",
      "tray reaches its lower stop",
      "ball1 touches ball2",
      "ball2 touches block",
      "block drops through hoop",
      "block comes to rest in bin"
    ]
  },
  {
    "id": "elevator",
    "brief": "weight falls 0.5 m onto lever, whose rising end crosses a gap to push lift upward; lever reaches its lower stop before lift crosses another gap and strikes ball across bridge into cup where it rests.",
    "things": [
      {"name": "weight", "kind": "loose", "what": "lever weight"},
      {"name": "lever", "kind": "hinged", "what": "lifting lever"},
      {"name": "lift", "kind": "sliding", "what": "vertical striker"},
      {"name": "ball", "kind": "loose", "what": "target ball"},
      {"name": "bridge", "kind": "fixed", "what": "ball bridge"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "weight touches lever",
      "lever touches lift",
      "lever reaches its lower stop",
      "lift touches ball",
      "ball comes to rest in cup"
    ]
  },
  {
    "id": "pendulums",
    "brief": "pend1 released from 0.7 m above its lowest point strikes pend2, pend2 strikes cart, and cart opens flap to its lower stop, releasing ball through hoop into box where it rests.",
    "things": [
      {"name": "pend1", "kind": "hinged", "what": "first pendulum"},
      {"name": "pend2", "kind": "hinged", "what": "second pendulum"},
      {"name": "cart", "kind": "sliding", "what": "impact cart"},
      {"name": "flap", "kind": "hinged", "what": "release flap"},
      {"name": "ball", "kind": "loose", "what": "released ball"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "pend1 touches pend2",
      "pend2 touches cart",
      "cart touches flap",
      "flap reaches its lower stop",
      "ball drops through hoop",
      "ball comes to rest in box"
    ]
  },
  {
    "id": "collapse",
    "brief": "ball starts 0.8 m up ramp and knocks key from beneath bridge1, making bridge1 fall into bridge2; bridge2 hits flap, which reaches its lower stop and releases payload into bin where it rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "support-removing ball"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "key", "kind": "sliding", "what": "bridge support"},
      {"name": "bridge1", "kind": "loose", "what": "first falling bridge"},
      {"name": "bridge2", "kind": "loose", "what": "second bridge block"},
      {"name": "flap", "kind": "hinged", "what": "payload release"},
      {"name": "payload", "kind": "loose", "what": "final block"},
      {"name": "bin", "kind": "fixed", "what": "catching bin"}
    ],
    "test": [
      "ball touches key",
      "bridge1 touches bridge2",
      "bridge2 touches flap",
      "flap reaches its lower stop",
      "payload comes to rest in bin"
    ]
  },
  {
    "id": "turnstile",
    "brief": "ball1 starts 1 m up ramp and strikes rotor, which turns into ball2; ball2 pushes latch away and releases block through ring into box where it rests.",
    "things": [
      {"name": "ball1", "kind": "loose", "what": "rotor trigger"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "rotor", "kind": "hinged", "what": "armed turnstile"},
      {"name": "ball2", "kind": "loose", "what": "latch striker"},
      {"name": "latch", "kind": "sliding", "what": "block support"},
      {"name": "block", "kind": "loose", "what": "released payload"},
      {"name": "ring", "kind": "fixed", "what": "drop opening"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "ball1 touches rotor",
      "rotor touches ball2",
      "ball2 touches latch",
      "block drops through ring",
      "block comes to rest in box"
    ]
  },
  {
    "id": "wedge",
    "brief": "trigger drops 0.5 m onto wedge, driving wedge down until it contacts cart and forces cart sideways; cart knocks block off ledge so block drops through hoop into box and rests.",
    "things": [
      {"name": "trigger", "kind": "loose", "what": "falling trigger"},
      {"name": "wedge", "kind": "sliding", "what": "vertical motion converter"},
      {"name": "cart", "kind": "sliding", "what": "sideways striker"},
      {"name": "block", "kind": "loose", "what": "falling payload"},
      {"name": "ledge", "kind": "fixed", "what": "payload ledge"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "trigger touches wedge",
      "wedge touches cart",
      "cart touches block",
      "block drops through hoop",
      "block comes to rest in box"
    ]
  },
  {
    "id": "halfpipe",
    "brief": "ball1 starts 1 m up ramp, crosses halfpipe and climbs its far side to hit block; block strikes pendulum, which knocks ball2 through hoop into cup where it rests.",
    "things": [
      {"name": "ball1", "kind": "loose", "what": "halfpipe ball"},
      {"name": "ramp", "kind": "fixed", "what": "approach ramp"},
      {"name": "halfpipe", "kind": "fixed", "what": "curved track"},
      {"name": "block", "kind": "loose", "what": "pendulum striker"},
      {"name": "pendulum", "kind": "hinged", "what": "final striker"},
      {"name": "ball2", "kind": "loose", "what": "falling target ball"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "ball1 touches block",
      "block touches pendulum",
      "pendulum touches ball2",
      "ball2 drops through hoop",
      "ball2 comes to rest in cup"
    ]
  },
  {
    "id": "catchcart",
    "brief": "ball1 falls 0.6 m through hoop onto the sloped back of cart, sending cart into flap; flap reaches its lower stop and releases ball2 into box where it rests.",
    "things": [
      {"name": "ball1", "kind": "loose", "what": "falling drive ball"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "cart", "kind": "sliding", "what": "sloped catching cart"},
      {"name": "flap", "kind": "hinged", "what": "release flap"},
      {"name": "ball2", "kind": "loose", "what": "released ball"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "ball1 drops through hoop",
      "ball1 touches cart",
      "cart touches flap",
      "flap reaches its lower stop",
      "ball2 comes to rest in box"
    ]
  },
  {
    "id": "balance",
    "brief": "ball1 starts 0.9 m up ramp and rolls into the recessed end of balance, driving balance to its lower stop and dislodging block from the other end; block hits ball2, which drops through hoop into cup and rests.",
    "things": [
      {"name": "ball1", "kind": "loose", "what": "balance weight"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "balance", "kind": "hinged", "what": "two-ended balance"},
      {"name": "block", "kind": "loose", "what": "dislodged striker"},
      {"name": "ball2", "kind": "loose", "what": "final ball"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "ball1 touches balance",
      "balance reaches its lower stop",
      "block touches ball2",
      "ball2 drops through hoop",
      "ball2 comes to rest in cup"
    ]
  },
  {
    "id": "ricochet",
    "brief": "ball starts 1 m above wall1 and falls to ricochet from wall1 into wall2 and then target; target reaches its lower stop and releases block into bin where it rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "ricochet ball"},
      {"name": "wall1", "kind": "fixed", "what": "first angled wall"},
      {"name": "wall2", "kind": "fixed", "what": "second angled wall"},
      {"name": "target", "kind": "hinged", "what": "release target"},
      {"name": "block", "kind": "loose", "what": "released payload"},
      {"name": "bin", "kind": "fixed", "what": "catching bin"}
    ],
    "test": [
      "ball touches wall1",
      "ball touches wall2",
      "ball touches target",
      "target reaches its lower stop",
      "block comes to rest in bin"
    ]
  },
  {
    "id": "crossslides",
    "brief": "ball drops 0.4 m onto slider1, pushing slider1 across a gap into slider2; slider2 withdraws the support beneath block so block falls through hoop into box and rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "slide trigger"},
      {"name": "slider1", "kind": "sliding", "what": "first slide"},
      {"name": "slider2", "kind": "sliding", "what": "crosswise slide"},
      {"name": "block", "kind": "loose", "what": "released payload"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "ball touches slider1",
      "slider1 touches slider2",
      "block drops through hoop",
      "block comes to rest in box"
    ]
  },
  {
    "id": "hammer",
    "brief": "ball starts 0.8 m up ramp and knocks prop away, releasing hammer to swing into peg; peg crosses a gap and knocks block through hoop into cup where it rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "support trigger"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "prop", "kind": "sliding", "what": "hammer support"},
      {"name": "hammer", "kind": "hinged", "what": "falling hammer"},
      {"name": "peg", "kind": "sliding", "what": "driven striker"},
      {"name": "block", "kind": "loose", "what": "final payload"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "ball touches prop",
      "hammer touches peg",
      "peg touches block",
      "block drops through hoop",
      "block comes to rest in cup"
    ]
  },
  {
    "id": "tipwedge",
    "brief": "block falls 0.5 m onto one side of wedge, tipping the loose wedge into ball1; ball1 rolls into flap, which reaches its lower stop and releases ball2 into cup where it rests.",
    "things": [
      {"name": "block", "kind": "loose", "what": "falling tip weight"},
      {"name": "wedge", "kind": "loose", "what": "free tipping wedge"},
      {"name": "ball1", "kind": "loose", "what": "flap striker"},
      {"name": "ramp", "kind": "fixed", "what": "ball guide"},
      {"name": "flap", "kind": "hinged", "what": "release flap"},
      {"name": "ball2", "kind": "loose", "what": "released ball"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "block touches wedge",
      "wedge touches ball1",
      "ball1 touches flap",
      "flap reaches its lower stop",
      "ball2 comes to rest in cup"
    ]
  },
  {
    "id": "slides",
    "brief": "trigger starts 0.7 m up ramp and hits slider1, slider1 crosses a gap to hit weight, weight strikes slider2, and slider2 knocks payload through hoop into bin where it rests.",
    "things": [
      {"name": "trigger", "kind": "loose", "what": "rolling trigger"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "slider1", "kind": "sliding", "what": "first striker"},
      {"name": "weight", "kind": "loose", "what": "middle striker"},
      {"name": "slider2", "kind": "sliding", "what": "second striker"},
      {"name": "payload", "kind": "loose", "what": "final block"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "bin", "kind": "fixed", "what": "catching bin"}
    ],
    "test": [
      "trigger touches slider1",
      "slider1 touches weight",
      "weight touches slider2",
      "slider2 touches payload",
      "payload drops through hoop",
      "payload comes to rest in bin"
    ]
  },
  {
    "id": "rollingring",
    "brief": "ball starts 1 m up ramp and descends through hoop before striking ring, which rolls into slider; slider knocks block into box where it rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "airborne trigger ball"},
      {"name": "ramp", "kind": "fixed", "what": "launch ramp"},
      {"name": "hoop", "kind": "fixed", "what": "flight hoop"},
      {"name": "ring", "kind": "loose", "what": "rolling rigid ring"},
      {"name": "slider", "kind": "sliding", "what": "block striker"},
      {"name": "block", "kind": "loose", "what": "final payload"},
      {"name": "box", "kind": "fixed", "what": "catching box"}
    ],
    "test": [
      "ball drops through hoop",
      "ball touches ring",
      "ring touches slider",
      "slider touches block",
      "block comes to rest in box"
    ]
  },
  {
    "id": "deflectors",
    "brief": "ball falls 1 m through hoop onto flap1, which swings to its lower stop and redirects ball onto flap2; flap2 reaches its lower stop and sends ball down chute into cup where it rests.",
    "things": [
      {"name": "ball", "kind": "loose", "what": "descending ball"},
      {"name": "hoop", "kind": "fixed", "what": "entry hoop"},
      {"name": "flap1", "kind": "hinged", "what": "first deflector"},
      {"name": "flap2", "kind": "hinged", "what": "second deflector"},
      {"name": "chute", "kind": "fixed", "what": "final guide"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "ball drops through hoop",
      "ball touches flap1",
      "flap1 reaches its lower stop",
      "ball touches flap2",
      "flap2 reaches its lower stop",
      "ball comes to rest in cup"
    ]
  },
  {
    "id": "cam",
    "brief": "cylinder starts 1 m up ramp and strikes cam, whose turning lobe crosses a gap to push follower; follower knocks ball off shelf so ball drops through hoop into cup and rests.",
    "things": [
      {"name": "cylinder", "kind": "loose", "what": "rolling cam driver"},
      {"name": "ramp", "kind": "fixed", "what": "starting ramp"},
      {"name": "cam", "kind": "hinged", "what": "lobed cam"},
      {"name": "follower", "kind": "sliding", "what": "cam follower"},
      {"name": "ball", "kind": "loose", "what": "falling target ball"},
      {"name": "shelf", "kind": "fixed", "what": "ball shelf"},
      {"name": "hoop", "kind": "fixed", "what": "drop hoop"},
      {"name": "cup", "kind": "fixed", "what": "catching cup"}
    ],
    "test": [
      "cylinder touches cam",
      "cam touches follower",
      "follower touches ball",
      "ball drops through hoop",
      "ball comes to rest in cup"
    ]
  }
]
```