# Impulsion

[← Retour aux 72 enchantements](../../Enchantements-FR.md)

**Identifiant :** `golems_materiaux:impulsion`  
**Supports :** Canne à carotte / Canne à champignon biscornu  
**Niveau maximum :** 1 (I)  
**Poids de génération dans la définition :** 3  
**Coût d'enclume déclaré :** 1

## Effet

Prolonge le boost des cochons et arpenteurs montés.

> **État de vérification :** synthèse de l'implémentation Java et des ressources du JAR 1.13.1 ; à confirmer en jeu (conditions, chances, acquisition et équilibrage). Un `effects` JSON vide ne signifie pas un enchantement inactif.

## Liste exacte des objets compatibles dans le tag

- `minecraft:carrot_on_a_stick`
- `minecraft:warped_fungus_on_a_stick`

## Références internes du mod

- Déclaration : `data/golems_materiaux/enchantment/impulsion.json`
- Tag d'objets : `data/golems_materiaux/tags/item/enchantable/impulsion.json`
- `mixin.AncientPigBoostMixin.gm$longer`
- `mixin.AncientStriderBoostMixin.gm$longer`
