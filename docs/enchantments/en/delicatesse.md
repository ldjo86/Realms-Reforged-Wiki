# Delicacy

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:delicatesse`  
**Applicable to:** Brush  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Extends the time before brushing progress resets.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:brush`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/delicatesse.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/delicatesse.json`
- `mixin.AncientBrushMixin.gm$gentle`
