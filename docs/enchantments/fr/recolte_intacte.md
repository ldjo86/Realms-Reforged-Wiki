# Récolte intacte

[← Retour aux 72 enchantements](../../Enchantements-FR.md)

**Identifiant :** `golems_materiaux:recolte_intacte`  
**Supports :** Cisailles  
**Niveau maximum :** 1 (I)  
**Poids de génération dans la définition :** 3  
**Coût d'enclume déclaré :** 1

## Effet

Permet certaines récoltes intactes avec les cisailles, notamment sur les ruches.

> **État de vérification :** synthèse de l'implémentation Java et des ressources du JAR 1.13.1 ; à confirmer en jeu (conditions, chances, acquisition et équilibrage). Un `effects` JSON vide ne signifie pas un enchantement inactif.

## Liste exacte des objets compatibles dans le tag

- `minecraft:shears`

## Références internes du mod

- Déclaration : `data/golems_materiaux/enchantment/recolte_intacte.json`
- Tag d'objets : `data/golems_materiaux/tags/item/enchantable/recolte_intacte.json`
- `AncientTools.drops`
- `mixin.AncientBeehiveMixin.gm$intact`
- `mixin.AncientBeehiveMixin.gm$keepBees`
