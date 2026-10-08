# Leader

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:leader`  
**Applicable to:** Helmets  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Helmet enchantment linked to leading and commanding companions.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `golems_materiaux:diamond_crowned_helmet_1` — Diamond Crowned Helmet — Skeleton
- `golems_materiaux:diamond_crowned_helmet_2` — Diamond Crowned Helmet — Zombie
- `golems_materiaux:diamond_crowned_helmet_3` — Diamond Crowned Helmet — Skeleton + Zombie
- `golems_materiaux:diamond_crowned_helmet_4` — Diamond Crowned Helmet — Creeper
- `golems_materiaux:diamond_crowned_helmet_5` — Diamond Crowned Helmet — Skeleton + Creeper
- `golems_materiaux:diamond_crowned_helmet_6` — Diamond Crowned Helmet — Zombie + Creeper
- `golems_materiaux:diamond_crowned_helmet_7` — Diamond Crowned Helmet — Skeleton + Zombie + Creeper
- `golems_materiaux:netherite_crowned_helmet_1` — Netherite Crowned Helmet — Skeleton
- `golems_materiaux:netherite_crowned_helmet_2` — Netherite Crowned Helmet — Zombie
- `golems_materiaux:netherite_crowned_helmet_3` — Netherite Crowned Helmet — Skeleton + Zombie
- `golems_materiaux:netherite_crowned_helmet_4` — Netherite Crowned Helmet — Creeper
- `golems_materiaux:netherite_crowned_helmet_5` — Netherite Crowned Helmet — Skeleton + Creeper
- `golems_materiaux:netherite_crowned_helmet_6` — Netherite Crowned Helmet — Zombie + Creeper
- `golems_materiaux:netherite_crowned_helmet_7` — Netherite Crowned Helmet — Skeleton + Zombie + Creeper
- `minecraft:chainmail_helmet`
- `minecraft:copper_helmet`
- `minecraft:diamond_helmet`
- `minecraft:golden_helmet`
- `minecraft:iron_helmet`
- `minecraft:leather_helmet`
- `minecraft:netherite_helmet`
- `minecraft:turtle_helmet`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/leader.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/leader.json`
- `AncientEnchantments.lambda$offer$0`
- `LeaderOrders.lambda$roster$0`
