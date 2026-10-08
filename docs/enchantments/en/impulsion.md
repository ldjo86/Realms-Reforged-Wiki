# Impulse

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:impulsion`  
**Applicable to:** Carrot on a stick / Warped fungus on a stick  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Extends the boost duration for ridden pigs and striders.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:carrot_on_a_stick`
- `minecraft:warped_fungus_on_a_stick`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/impulsion.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/impulsion.json`
- `mixin.AncientPigBoostMixin.gm$longer`
- `mixin.AncientStriderBoostMixin.gm$longer`
