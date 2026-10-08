# Recovery

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:recuperation`  
**Applicable to:** Chestplates / Horse armor / Wolf armor  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Slowly restores health after a period without taking damage.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:chainmail_chestplate`
- `minecraft:copper_chestplate`
- `minecraft:copper_horse_armor`
- `minecraft:diamond_chestplate`
- `minecraft:diamond_horse_armor`
- `minecraft:golden_chestplate`
- `minecraft:golden_horse_armor`
- `minecraft:iron_chestplate`
- `minecraft:iron_horse_armor`
- `minecraft:leather_chestplate`
- `minecraft:leather_horse_armor`
- `minecraft:netherite_chestplate`
- `minecraft:netherite_horse_armor`
- `minecraft:wolf_armor`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/recuperation.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/recuperation.json`
- `AncientEffects.tick`
