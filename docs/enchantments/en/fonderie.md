# Smelting

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:fonderie`  
**Applicable to:** Pickaxes  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Automatically smelts certain mined block drops.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:copper_pickaxe`
- `minecraft:diamond_pickaxe`
- `minecraft:golden_pickaxe`
- `minecraft:iron_pickaxe`
- `minecraft:netherite_pickaxe`
- `minecraft:stone_pickaxe`
- `minecraft:wooden_pickaxe`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/fonderie.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/fonderie.json`
- `AncientTools.drops`
