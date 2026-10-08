# Vampirism

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:vampirisme`  
**Applicable to:** Swords  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Heals the killer by 2 health points after a kill with the weapon.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:copper_sword`
- `minecraft:diamond_sword`
- `minecraft:golden_sword`
- `minecraft:iron_sword`
- `minecraft:netherite_sword`
- `minecraft:stone_sword`
- `minecraft:wooden_sword`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/vampirisme.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/vampirisme.json`
- `AncientEffects.kill`
