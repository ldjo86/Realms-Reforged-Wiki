# Player graves and survival utilities

## Player Grave

The project advertises a tomb on death which stores inventory, equipment and experience. The grave remembers its owner; the translation file contains `golems.grave.owner_only` (only the rightful player may open it). The CurseForge description says overflowing inventory remains safely inside until recovery. Verify retrieval and server ownership rules in a test world before relying on the system in hardcore or multiplayer.

## Healing Standard

Stores up to **64 Golden Flowers** and heals nearby allies **outside combat** in an advertised ~8-block radius. The mod has a dedicated `HealingStandard` implementation and user-facing translated supply text.

## Diamond Anvil

A special anvil with **normal, chipped and damaged** states, and dedicated Java cost logic. A shaped crafting definition is provided in the [recipe catalog](Recipes-EN.md).

## Other survival and combat systems

Golden Elixir / Splash Golden Elixir, explosive arrows and shield, charged TNT, ancient bow and necromantic staff, loot from Masters, crowned helmets, companion banners, and experience bounty bottles. See the [items index](Items-index-EN.md).
