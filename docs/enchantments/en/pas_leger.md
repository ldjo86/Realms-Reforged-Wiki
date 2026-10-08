# Light Steps

[← Back to all 72 enchantments](../../Enchantments-EN.md)

**Registry ID:** `golems_materiaux:pas_leger`  
**Applicable to:** Boots  
**Maximum level:** 1 (I)  
**Data-defined weight:** 3  
**Data-defined anvil cost:** 1

## What it does

Makes movement harder for vibration sensors to detect.

> **Verification level:** description inferred from Java handlers and packaged data in the 1.13.1 JAR; gameplay triggers, probabilities, acquisition and balance have not been verified in-game. An empty `effects` JSON object does not mean the enchantment has no Java effect.

## Exact supported-item tag entries

- `minecraft:chainmail_boots`
- `minecraft:copper_boots`
- `minecraft:diamond_boots`
- `minecraft:golden_boots`
- `minecraft:iron_boots`
- `minecraft:leather_boots`
- `minecraft:netherite_boots`

## Internal evidence

- Definition: `data/golems_materiaux/enchantment/pas_leger.json`
- Applicable-items tag: `data/golems_materiaux/tags/item/enchantable/pas_leger.json`
- `mixin.AncientStealthMixin.gm$quiet`
