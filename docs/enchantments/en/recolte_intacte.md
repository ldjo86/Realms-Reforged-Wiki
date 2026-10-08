# Intact Harvest

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:recolte_intacte`  
**Applicable to:** Shears  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Allows intact gathering of some objects with shears, including beehives.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:shears`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/recolte_intacte.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/recolte_intacte.json`
- `AncientTools.drops`
- `mixin.AncientBeehiveMixin.gm$intact`
- `mixin.AncientBeehiveMixin.gm$keepBees`
