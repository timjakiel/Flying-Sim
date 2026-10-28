# Cape Crusher

You're a supervillain taking Skyline City by force. Five heroes stand in your way, and every one you put down gets back up and comes back with friends.

Open `index.html` in a browser (needs internet for Three.js from the CDN).

## Status
Built in stages. **Stages 1 to 3 are done:** you play the villains, the heroes are the bosses, wrecking the city brings the law down on you, and full runs are in.

| Stage | What | Status |
| --- | --- | --- |
| 1 | The flip: villains playable, heroes as bosses, Practice fights | Done |
| 2 | Heat and henchmen: cops, SWAT, helicopters, tanks, drones; loot from destruction | Done |
| 3 | The run: 24 rounds of waves and bosses, health carry-over, stacking heroes, tag-team | Done |
| 4 | Power-ups every 5 rounds (replaced the Black Market) | Done |
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
Pick your villain and a difficulty on the main menu. A run is 24 rounds in five acts: three wave rounds before the first boss, then four wave rounds before each of the others.

- **Wave rounds:** no wanted stars. Each round throws waves of henchmen at you (2 waves early, up to 4 late) and you clear every last one. The waves grow every round and new units join as you go: cops and cop cars from round 1, SWAT from 3, gunships from 4, drones from 7, tanks from 11. Every henchman has a red diamond over it that shows through buildings (orange for gunships and tanks), and a radar in the corner shows everything around you with your heading up. Stragglers that fall far behind get sent back in closer, and the last few get a distance marker.
- **Bosses:** four random heroes, then your mirror in Act 5. Every hero you beat comes back for each later boss fight at 60% health with one power fewer. Only two attack at once; the rest circle and tag in when one drops.
- **Power Up, every 5 rounds:** after each boss you get 3 points to level Strength (punches), your three powers, or Meteor Slam. Each level is +25% damage and size, max 5.
- Health and loot carry through the run. No health regen: +15% after each wave round, +35% after a boss. Get knocked out and the run's over.
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

Fly through foot soldiers and cars to flatten them; every power, explosion and collapse hurts them too, and rooftop shooters fall with their building. Buildings block their shots. Gunships spin in and explode, tanks take a few hits. Heat stars are only in Rampage now; runs use waves.

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
| Right-click / V | Use the power (hold for beams; 5 s of straight firing overheats a beam for 5 s, and it cools while you're not firing) |
| R | Back to the sky |
| P / Esc | Pause |
| N | Music on/off |
| M | Mute |

On phones: left stick flies, drag to look, buttons for boost, punch, slam and powers.

Buildings are solid at cruising speed: you slide along walls and land on roofs. You only smash through while boosting (or still going boost speed), punch-dashing, launching, meteor-slamming or using a power.
