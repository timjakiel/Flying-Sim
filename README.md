# Cape Crusher

You're a supervillain taking Skyline City by force. Five heroes stand in your way, and every one you put down gets back up and comes back with friends.

Open `index.html` in a browser (needs internet for Three.js from the CDN).

## Status
Built in stages. **Stage 1 (the flip) is done:** you play the villains, the heroes are the bosses, and the permanent power shop is gone.

| Stage | What | Status |
| --- | --- | --- |
| 1 | The flip: villains playable, heroes as bosses, Practice fights | Done |
| 2 | Heat and henchmen: cops, SWAT, helicopters, tanks, drones; loot from destruction | Next |
| 3 | The run: 5 acts, route map, stops, health carry-over, stacking heroes, tag-team | Planned |
| 4 | Schemes: pick-1-of-3 upgrades, Black Market, in-run power boosts | Planned |
| 5 | Polish: team-ups, Phase 2, mid-fight trash talk, Hall of Infamy, balance | Planned |

## Villains (playable)
Every villain flies, punch-dashes (left-click) and meteor-slams (X), plus three powers: **mouse wheel** or 1/2/3 picks one, **right-click** or V uses it (hold for beams).

| Villain | 1 | 2 | 3 (hold) | Mirror hero |
| --- | --- | --- | --- | --- |
| The Warlord | Super Shout | Thunder Clap | Laser Vision | Skybreaker |
| Scorch | Fireball | Supernova | Flamethrower | Blaze |
| Psyche | Psychic Push | Rip & Hurl | Gravity Well | Mindstorm |
| Overload | Lightning Bolt | EMP Burst | Thunderstorm | Volt |
| Permafrost | Ice Spikes | Blizzard | Ice Beam | Frostbite |

## Heroes (bosses)
Each hero mirrors one villain's powers, plus a ramming dash and meteor slam. Attacks glow in the hero's color before they land. Every fight opens with a cut scene: the hero drops in, gets a title card and talks trash.

| Hero | Says |
| --- | --- |
| Skybreaker | "Pick on someone your own size." |
| Blaze | "You burn this city, I burn you." |
| Mindstorm | "I can hear what you're planning. It's stupid." |
| Volt | "Power down. Now." |
| Frostbite | "Chill out. Permanently." |

## Modes
- **Practice** (main menu): pick any heroes (tap to add or remove, up to 1v5) and a difficulty, and fight. Full runs arrive in Stage 3.
- **Sandbox** (side game): every power at max, no clock, rebuild the city any time.
- **Rampage** (side game): two-minute rounds scored on collateral damage.

| Difficulty | Hero health | Hero damage | Speed / aim | Hero power level |
| --- | --- | --- | --- | --- |
| Easy | 700 | 40% | slow, sloppy aim, long tells | 1 |
| Normal | 1,300 | 70% | leads shots | 3 |
| Hard | 2,200 | 120% | fast, tight aim, short tells | 5 |

## The city
Every building breaks into chunks: punch hero-sized holes, and floors that lose too much support collapse onto what's left. Diving into the street leaves cracked craters. Gas cans, oil drums, propane tanks and fuel tankers explode in chain reactions; trees snap and cars get crushed or thrown.

## Suits
Cosmetic. Every achievement unlocks one (Rampage rounds count, as does crushing every hero on Hard; Sandbox never does). **Signature** keeps each villain in their own colors.

## Music
Synthesized live: a menu theme, a tense intro under the cut scene, a 150 bpm battle score that gets more frantic when someone is low, and a fanfare or sting at the end. **N** toggles music, **M** mutes everything.

## Performance
**Graphics** on the main menu cycles Auto / Low / Medium / High (applies on the next page load). Auto picks Low on integrated graphics. Untouched buildings are merged into 64 batches, render resolution adapts to frame time, and the top-right shows FPS.

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

On phones: left stick flies, drag to look, buttons for boost, punch, slam and powers.
