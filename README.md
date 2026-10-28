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
Each hero mirrors one villain's powers, plus a ramming dash and meteor slam. Attacks glow in the hero's color before they land. Every fight opens with a hero reveal: a hazard-stripe "WARNING · HERO APPROACHING" banner, then the hero's colors wipe across the screen with their name scrolling huge behind them, a studio-lit portrait rendered from the actual model rises in, and the name plate slams down. Then each hero drops in, gets a title card and talks trash.

| Hero | Says |
| --- | --- |
| Skybreaker | "Pick on someone your own size." |
| Blaze | "You burn this city, I burn you." |
| Mindstorm | "I can hear what you're planning. It's stupid." |
| Volt | "Power down. Now." |
| Frostbite | "Chill out. Permanently." |

## The run
Pick your villain and a difficulty on the main menu. A run is 24 rounds in five acts: three wave rounds before the first boss, then four wave rounds before each of the others.

- **Wave rounds:** no wanted stars. Each round marks spawner buildings with colored light beams: a **precinct** (cops, cop cars, snipers), an **armory** (SWAT, riot shields, net gunners, tanks, mechs; from round 3) and a **helipad** tower (gunships, drones, jetpack troopers; from round 4). They keep sending henchmen, faster the longer they stand, until you level them. Leveling the last spawner triggers the **last stand**: a final surge of henchmen dropped in around you, and the round ends when every henchman is dead. During the last stand, stragglers more than about 250 m away get pulled back in close, so they come to you instead of you hunting them. Henchmen never spawn inside buildings. Henchmen hit hard and get deadlier every round (about x2 damage in round 1, x2.7 by round 24, with sharper aim), and speed alone no longer makes you untouchable. Each one you level pays a bonus. Every henchman has a diamond tag that shows through buildings, and a marker points to the nearest spawner still standing.
- **Elites** unlock as the run goes: riot shields (round 5) block anything flying into their front, so hit them from behind or above. Snipers (6) paint you with a red laser before a heavy shot, so move fast or get behind a building. Net gunners (10) pin you until you mash keys. Jetpack troopers (11) chase you through the air. Mechs (15) walk straight through buildings and super-punch you.
- **Heavier hardware** as the run goes: rooftop artillery (round 8) lobs high-arcing shells, marked by a red ring where they'll land, that fling you into a tumble. Black Hawks (10) bring door gunners and rockets, Apaches (15) chain guns and four-rocket salvos, and fighter jets (17) make strafing runs with guns and homing missiles, with a sonic boom as they pass. Tanks roll out in bigger numbers every few rounds.
- **Round modifiers** (most rounds from round 2, shown before you start): Gas Leak (every henchman explodes when they go down), Blackout (night), Tank Parade, Air Raid, Double or Nothing (twice the henchmen, twice the loot).
- **Boss cameo:** in the last wave round before each boss, the act's hero shows up, hangs in the sky for a second ("INCOMING! KEEP MOVING"), then dives at you. Stopped or moving slowly, it locks on and lands a super punch that sends you tumbling through the buildings. Flying fast, you can outrun the turn and dodge it. Either way they talk trash and leave.
- **Style meter:** chain kills within 3.5 s to climb D, C, B, A, S, SS, SSS. Each rank adds 25% to henchman loot.
- **Health orbs:** gunships, tanks and mechs always drop one, elites often, regular henchmen sometimes. They drift to you when you're close.
- **Rage:** fills from kills, leveled spawners and hits on heroes. When it's full, **G** unleashes your villain's ultimate: Sonic Boom, Meltdown, Mass Hurl, Skyfall or Absolute Zero. Rage carries over between rounds.
- **Bosses:** four random heroes, then your mirror in Act 5. Every hero you beat comes back for each later boss fight at 60% health with one power fewer. Only two attack at once; the rest circle and tag in when one drops.
- **Power Up, every 5 rounds:** after each boss you get 3 points to level Strength (punches), your three powers, or Meteor Slam. Each level is +25% damage and size, max 5.
- The city and your position carry over the whole run: every round picks up where the last one ended, with all the damage still there, and bosses drop in on the streets ahead of you. Only a new run rebuilds the city.
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
Three recorded tracks live in `audio/`. Browsers often block a page from fetching files (the artifact viewer, file viewers, opening it from disk), so `index.html` has the songs packed inside it. **Edit `src/game.html`**, then run `python3 tools/build.py` to rebuild `index.html`. The tracks are: the menu theme (`menu-theme.mp3`, "Dramatic Villain Reveal" with choir chants), the wave-round theme (`waves-theme.mp3`, "Battle") and the boss theme (`boss-theme.mp3`, "To the Death"), which kicks in the moment a hero shows up and runs through the fight. Both are trimmed to loop. If a file can't load, the synthesized version plays instead. Everything else is synthesized live: a tense intro under the cut scene, a 150 bpm battle score that gets more frantic when someone is low, and a fanfare or sting at the end. **N** toggles music, **M** mutes everything, on the menus too.

## Performance
**Graphics** on the main menu cycles Auto / Low / Medium / High (applies on the next page load). Auto picks Low on integrated graphics. Untouched buildings are merged into 64 batches, render resolution adapts to frame time, and the top-right shows FPS.

## Controls
| Key | Action |
| --- | --- |
| Mouse | Steer / look (click to lock the mouse). The dot in the middle is where powers land; it turns red over an enemy |
| W A S D | Fly |
| Space / E | Rise |
| Q / C | Descend |
| Shift | Supersonic boost |
| Click / F | Punch-dash |
| X | Launch / meteor slam |
| Mouse wheel / 1 2 3 | Pick a power |
| Right-click / V | Use the power (hold for beams; 5 s of straight firing overheats a beam for 5 s, and it cools while you're not firing) |
| G | Rage ultimate, when the bar is full |
| R | Back to the sky |
| P / Esc | Pause |
| N | Music on/off |
| M | Mute |

On phones: left stick flies, drag to look, buttons for boost, punch, slam and powers.

A punch-dash that connects is a super punch: the hero ragdolls about 150 m (500 ft), spinning with limbs flailing, and a hero's ram does the same to you. Bursting into a building sets off one small explosion.

Buildings are solid at cruising speed: you slide along walls and land on roofs. You only smash through while boosting (or still going boost speed), punch-dashing, launching, meteor-slamming or using a power.
