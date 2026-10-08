# Prospecting

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:prospection`  
**Applicable to:** Shovels  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Adds a small chance of bonus drops when digging sand or gravel.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:copper_shovel`
- `minecraft:diamond_shovel`
- `minecraft:golden_shovel`
- `minecraft:iron_shovel`
- `minecraft:netherite_shovel`
- `minecraft:stone_shovel`
- `minecraft:wooden_shovel`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/prospection.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/prospection.json`
- `AncientTools.drops`
