# Enchanted Blossom

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:floraison_enchantee`  
**Applicable to:** Golden sapling  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Alters the growth or rewards of an enchanted golden sapling.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `golems_materiaux:golden_sapling` — Golden Sapling

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/floraison_enchantee.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/floraison_enchantee.json`
- `GoldenSaplingBlock.setPlacedBy`
- `AncientTools.drops`
