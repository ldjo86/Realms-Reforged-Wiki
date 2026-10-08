# Bounty hunting — Six ranks, waves and rewards

The **Bounty Hunter** profession gives access to contracts. A contract is accepted for free and gives a map leading to a hideout; clear enemy waves, retrieve the **Sealed Contract Chest**, and return it to a Bounty Hunter for the payment. Some missions include optional objectives (free a prisoner, recover a stolen relic, intercept a fleeing chief).

## Progression

| Rank | Hunt | Dedicated `.nbt` structure in 26.3 |
|---:|---|---|
| 1 | Infested Ruins | `hunts/ruins.nbt` |
| 2 | Occupied Hamlet | `hunts/hamlet.nbt` |
| 3 | Predator Cave | `hunts/cave.nbt` |
| 4 | Elite Fortress | `hunts/fortress.nbt` |
| 5 | Deep Necropolis | `hunts/necropolis.nbt` |
| 6 | Council of the Three Masters | No sixth distinct structure file found; final encounter is named in project and JAR locale |

The system has **multiple hostile waves**, captains and bonus missions. Some fights prevent skipping the night. **Fleeing or dying can forfeit the bounty**, although location loot may remain obtainable. Contracts require the Overworld and a non-Peaceful difficulty. Exact loot odds, unlock criteria and reward amounts have not been tested in-game.

**Evidence:** the five `data/golems_materiaux/structure/hunts/*.nbt` templates, `HuntRanks`, `HuntWaves`, `HuntRespawnMixin` and language keys, plus the official CurseForge project description.
