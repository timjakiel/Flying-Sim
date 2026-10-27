# Skybreaker

Fly around a big city like a certain yellow-and-blue superhero and punch straight through skyscrapers.

Open `index.html` in a browser (needs internet for Three.js from the CDN).

## The fight (main game)
Five supervillains are tearing the city apart. Pick your hero (**Hero** on the main menu), pick one or more villains and a difficulty, and take them down. Tap villains in the roster to add or remove them: pick two for a 2v1, or all five if you hate yourself. Fights have their own synthesized battle score: a tense drone and timpani build under the intro, a 150 bpm orchestral-style track (drums, driving bass, string ostinato, brass stabs and a hero theme) during the fight that gets more frantic when someone is close to going down, and a fanfare or sting at the end. **N** toggles the music (also in the pause menu), **M** mutes everything. Every fight opens with a short intro for each villain: he drops out of the sky, craters the street and gets a title card with his powers and a one-liner (click, tap or press Space to skip). Every villain in the fight gets his own health bar and screen marker, and multi-villain wins pay each villain's bounty plus 25%. Win to collect a bounty and spend it on power upgrades, which make you stronger in every fight. **Next villain** on the victory screen sends you straight into the next one.

| Villain | Mirror of | Powers (all villains also ram and meteor-slam) |
| --- | --- | --- |
| The Warlord | Skybreaker | Laser eyes, super shout, thunder clap |
| Scorch | Blaze | Fireballs, supernova, flamethrower |
| Psyche | Mindstorm | Thrown boulders, psychic push, gravity well (grabs you, then slams you down) |
| Overload | Volt | Lightning bolts (watch the ring that marks the strike), EMP (stuns you), thunderstorm |
| Permafrost | Frostbite | Ice spikes along the street, blizzard (slows you), ice beam (slows you) |

- Every attack glows in the villain's color before it lands, so dodge on the tell.
- Hurt them by flying into them fast (punch-dash hits hardest), with your hero's powers, meteor slams, or by blowing up explosives next to them. Explosions hurt you too.
- You heal slowly after four seconds without getting hit. A red marker always points to the villain.
- You fight with every power your hero has, at your shop level (minimum level 1).

| Difficulty | Villain health | Villain damage | Speed / aim | Villain power level | Bounty |
| --- | --- | --- | --- | --- | --- |
| Easy | 700 | 40% | slow, sloppy aim, long tells | 1 | $1M |
| Normal | 1,300 | 70% | leads his shots | 3 | $4M |
| Hard | 2,200 | 120% | fast, tight aim, short tells | 5 | $12M |

The menu marks which difficulties you've beaten for each villain and shows your fastest win.

## Side games
- **Sandbox**: fly around and wreck whatever you like with every power at max level. No clock. Pause and hit *Rebuild the city* for a fresh skyline.
- **Rampage**: two-minute rounds scored on the dollar value of everything you destroy. Each round pays you 0.4% of the damage plus a $50K appearance fee. Your best score is saved.

## Heroes
Pick a hero from **Hero** on the main menu. Everyone flies, punch-dashes (left-click) and meteor-slams (X). Each hero has three powers of their own: **mouse wheel** (or 1/2/3) picks one, **right-click** (or V) uses it, and you hold it for beams.

| Hero | 1 | 2 | 3 (hold) |
| --- | --- | --- | --- |
| Skybreaker: strength, sonic voice, laser eyes | Super Shout (cone) | Thunder Clap (around you) | Laser Vision |
| Blaze: fire | Fireball (exploding projectile) | Supernova (ring of fire) | Flamethrower |
| Mindstorm: telekinesis | Psychic Push (force cone) | Rip & Hurl (tear a chunk off the nearest building and throw it) | Gravity Well (lift everything, then slam it down) |
| Volt: lightning | Lightning Bolt (arcs to explosives and cars) | EMP Burst (stuns enemies) | Thunderstorm |
| Frostbite: ice | Ice Spikes (a line of spikes erupts ahead) | Blizzard (slows enemies) | Ice Beam |

## Powers
Sandbox has every power at max level; Showdown gives you every power at your shop level (minimum 1). In Rampage you buy them in the power shop, then pay to upgrade them (each level hits about 25% harder).

| Power | Buy | Lv 2 | Lv 3 | Lv 4 | Lv 5 |
| --- | --- | --- | --- | --- | --- |
| Meteor Slam (every hero) | $2.5M | $5.8M | $13.2M | $30.4M | $70.0M |
| Overtime (+30 s per level) | $6M | $15.6M | $40.6M | | |
| Titan Fists (every hero) | $15M | $36.0M | $86.4M | $207.4M | $497.7M |
| Each hero's power 1 | $8M | $18.4M | $42.3M | $97.3M | $223.9M |
| Each hero's power 2 | $12M | $27.6M | $63.5M | $146.0M | $335.8M |
| Each hero's power 3 | $20M | $44.0M | $96.8M | $213.0M | $468.5M |

## Explosives
Gas cans, oil drums, propane tanks and parked fuel tankers are scattered around the streets. Fly into one, laser it, or catch it in a blast and it goes up, setting off anything else nearby in a chain reaction.

## Suits
Every achievement unlocks a suit. Only Rampage rounds count toward them; Sandbox never does. Progress is saved in your browser.

| Suit | Achievement |
| --- | --- |
| Signature | Each hero in their own colors (default) |
| Classic | Unlocked from the start |
| Midnight | Wrecking Ball: wreck 400 buildings |
| Demolition | Urban Renewal: flatten 120 buildings to the street |
| Patriarch (with cape) | Skyline Edit: bring down the tops of 25 towers over 150 m |
| Crimson | Combo Breaker: hit a ×150 combo |
| Magenta | Car Juggler: send 500 cars flying |
| Stealth | Rampage Veteran: finish 30 Rampage rounds |
| Inferno | Superhero Landing: land 200 meteor slams |
| Ranger | Timber!: knock down 1,000 trees |
| Chrome | Sound Barrier: stay supersonic for 60 seconds straight |
| Hazmat | Chain Reaction: blow up 1,500 explosives |
| Warlord (with cape) | Nemesis: beat all five villains on Hard |
| Solid Gold (with cape) | Billionaire Problems: $10B of damage in one Rampage round |

## Performance
**Graphics** on the main menu cycles Auto / Low / Medium / High (takes effect the next time the page loads). Auto picks Low on Intel and other integrated or mobile graphics.

| | Low | Medium | High |
| --- | --- | --- | --- |
| Render resolution | 70% | 85% | 100% |
| Shadows | off | 1024 | 2048 soft |
| Antialiasing | off | off | on |
| View distance | 1.5 km | 2.6 km | 5 km |
| Debris / particles | 35% / 45% | 60% / 70% | full |
| Explosion lighting, rounder trees and clouds, richer music voices | off | partly | on |

On every setting, untouched buildings are merged into 64 batches (about 1,850 draw calls down to about 410), the render resolution drops automatically when frames run long, crater lighting only updates the dented patch, and the music is scheduled 0.6 s ahead so a frame hitch doesn't cut it out. The top-right corner shows FPS, the preset, and the current resolution if it has been lowered.

## Controls
| Key | Action |
| --- | --- |
| Mouse | Steer / look (click to lock the mouse) |
| W A S D | Fly |
| Space / E | Rise |
| Q / C | Descend |
| Shift | Supersonic boost |
| Click / F | Punch-dash |
| X | Launch / meteor slam |
| Mouse wheel / 1 2 3 | Pick a power |
| Right-click / V | Use the power (hold for beams) |
| R | Back to the sky |
| P / Esc | Pause |
| N | Music on/off |
| M | Mute |

On phones: left stick flies, drag to look, buttons for boost / punch / up / down.

## Destruction
- Buildings are made of chunks, so you punch a hole the size of you straight through them, and the concrete insides show.
- If a floor loses too much of its chunks, everything above it collapses, leaning toward the side you knocked out, and pancakes down onto whatever is left.
- Pieces that end up cut off from the ground fall too. You can punch falling chunks apart in mid-air.
- Dive into the street to leave a scorched crater. The shockwave wrecks nearby buildings, knocks trees flat and launches cars.
- **X** launches you off the street like a rocket, or drops you out of the sky into a superhero landing. Both leave spiderweb cracks in the ground.
- Trees snap when you fly through them, and collapsing buildings crush the cars under them.
