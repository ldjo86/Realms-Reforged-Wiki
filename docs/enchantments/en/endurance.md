# Endurance

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:endurance`  
**Applicable to:** Leggings  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Reduces some hunger costs from player actions.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:chainmail_leggings`
- `minecraft:copper_leggings`
- `minecraft:diamond_leggings`
- `minecraft:golden_leggings`
- `minecraft:iron_leggings`
- `minecraft:leather_leggings`
- `minecraft:netherite_leggings`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/endurance.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/endurance.json`
- `mixin.AncientHungerMixin.gm$endurance`
