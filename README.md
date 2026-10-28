# Cape Crusher

You're a supervillain taking Skyline City by force. Five heroes stand in your way, and every one you put down gets back up and comes back with friends.

Open `index.html` in a browser (needs internet for Three.js from the CDN).

## Status
Built in stages. **Stages 1 to 3 are done:** you play the villains, the heroes are the bosses, wrecking the city brings the law down on you, and full runs are in.

| Stage | What | Status |
| --- | --- | --- |
| 1 | The flip: villains playable, heroes as bosses, Practice fights | Done |
| 2 | Heat and henchmen: cops, SWAT, helicopters, tanks, drones; loot from destruction | Done |
| 3 | The run: 5 acts, route map, stops, health carry-over, stacking heroes, tag-team | Done |
| 4 | Schemes: pick-1-of-3 upgrades, Black Market, in-run power boosts | Next |
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

## The run
Pick your villain and a difficulty on the main menu. A run is five acts, about 20 minutes. Each act: choose one of two stops, twice, then fight the act's boss.

| Stop | What |
| --- | --- |
| Heist | Level the marked tower in 80 s. Pays $150K (more in later acts). |
| Ambush | Three armored trucks drive for the edge of town. $40K per truck you wreck. |
| Hostage | Hold the square for 40 s within 110 s. Heat never drops below ★★, and goes to ★★★ halfway. Pays $120K. |
| Sidekick | A smaller, weaker hero (Skylark, Ember, Echo, Spark, Flurry). Pays $80K. |
| Hideout | No fight. Heal 40%. |
| Black Market | Street doc (heal 30%, $60K), full patch-up ($150K), armor plating (-15% damage, stacks twice, $120K). Placeholder until Schemes. |

- Bosses: four random heroes, then your mirror in Act 5. Every hero you beat comes back for each later boss fight at 60% health with one power fewer. Only two attack at once; the rest circle and tag in when one drops.
- Health and loot carry through the run. No health regen; heal at a Hideout or the Black Market, and +25% after each boss. Wrecking stuff pays loot all run, including boss fights.
- Get knocked out and the run's over. The city rebuilds for every stop and fight.
- Records: runs, takeovers (wins), best haul, fastest win per villain and difficulty.

## Modes
- **Practice** (main menu): pick any heroes (tap to add or remove, up to 1v5) and a difficulty, and fight. Nothing on the line.
- **Sandbox** (side game): every power at max, no clock, rebuild the city any time.
- **Rampage** (side game): two minutes to grab as much loot as you can while the city fights back. Get your health to zero and you're busted.

| Difficulty | Hero health | Hero damage | Speed / aim | Hero power level |
| --- | --- | --- | --- | --- |
| Easy | 700 | 40% | slow, sloppy aim, long tells | 1 |
| Normal | 1,300 | 70% | leads shots | 3 |
| Hard | 2,200 | 120% | fast, tight aim, short tells | 5 |

## Heat and henchmen
Destruction pays **loot** (0.1% of the damage) and raises **Heat**. Lay low for 8 seconds and Heat starts to cool.

| Heat | What comes for you | Loot per kill |
| --- | --- | --- |
| ★ | Cops on streets and rooftops, cop cars that drive the road grid to you | cop $500, car $2,500 |
| ★★ | SWAT, plus a gunship with machine guns and rockets | SWAT $1,200, gunship $9,000 |
| ★★★ | Army tanks firing shells, and drone swarms | tank $18,000, drone $1,500 |

Fly through foot soldiers and cars to flatten them; every power, explosion and collapse hurts them too, and rooftop shooters fall with their building. Buildings block their shots. Gunships spin in and explode, tanks take a few hits. Heat is on in Rampage and during run stops.

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
