# Rapport d'audit technique du JAR 1.13.1

## Méthode

- Ouverture ZIP du JAR principal et des 5 JARs embarqués.
- Validation CRC et parsing de tous les JSON.
- Inspection des métadonnées Fabric, textures, tags d'enchantements et tables de recettes.
- Lecture des 235 classes du sous-module 26.3 par désassemblage Java ; repérage des points d'activation des 72 enchantements.
- Comparaison des fichiers des modules 26.1 et 26.3.

## Vérifications réussies

- CRC de l'archive : OK.
- 783 JSON lisibles dans le sous-module 26.3, aucune erreur syntaxique détectée.
- 72 déclarations d'enchantements et 72 tags `enchantable/` correspondants ; aucun tag manquant.
- 72 points d'activation repérés dans les classes Java.
- 291 clés de traduction présentes à la fois en français et en anglais (égalité des jeux de clés).

## Anomalies et améliorations recommandées

### P1 — Textures des quatre golems dupliquées dans le JAR 26.x

Une comparaison binaire du JAR `golems-materiaux-1.13.1-mc26.1-26.3-fabric.jar` montre **16 chemins PNG pour quatre contenus distincts** : tous les `gold.png`, `emerald.png`, `diamond.png` et `netherite.png` sont identiques (128 × 128 pixels) ; les fichiers de fissures pour chaque stade (`low`, `medium`, `high`) sont aussi identiques entre les quatre matériaux. La classe `GolemTextures.class` choisit les chemins par équipe (`dgp_gold`, `dgp_emerald`, `dgp_diamond`, `dgp_netherite`) mais ces chemins pointent vers des images au même contenu. La documentation présentait auparavant quatre aperçus côte à côte comme s'ils montraient quatre skins distincts : **présentation corrigée** dans les README, les pages Golems et la galerie. Les [empreintes SHA-256 de chaque PNG](../inventory/golem-texture-sha256.json) permettent de vérifier le diagnostic.

**À vérifier dans le projet du mod (pas corrigé dans le JAR ici) :** provenance des textures au build ; remplacer les 4 skins de base et 12 overlays par les ressources authentiques si elles doivent être propres à chaque matériau ; compiler et tester visuellement la sélection au rendu. Un JAR pour **Minecraft 1.21.x** est signalé par `INSTALLATION.md` mais n'est pas disponible dans cet audit ; ne pas affirmer que ses textures présentent la même anomalie.

### P1 — Traduction française corrompue

**39 valeurs** des 291 entrées françaises contiennent des séquences de mojibake. Exemples : `MaÃ®tre`, `BanniÃ¨re`, `Fragment dâ€™os`. La correction `patches/fr_fr-repaired.json` est proposée séparément, sans modifier le JAR d'origine. Vérifier visuellement les libellés en jeu après intégration.

### P2 — Textes d'entités non déclarés

Ces entités présentes dans `CustomEntities` n'ont pas de clé `entity.golems_materiaux.<id>` dans les fichiers de langue du sous-module :

- `illageois_demi_squelette`
- `illageois_zombifie`
- `demon_commandant`
- `goule`
- `illageois_gueri`

Ces clés devraient être ajoutées avec un nom français et anglais pour éviter un libellé générique en cas d'affichage par Minecraft.

### P2 — Recettes vanilla et interopérabilité

Le sous-module 26.3 contient **110 recettes dans `data/minecraft/recipe/`**. La substitution de recettes vanilla peut modifier la progression et entrer en conflit avec d'autres datapacks. La revue doit porter sur les changements de conception, pas simplement sur la syntaxe.

### P2 — Chargement des cinq versions embarquées

Les cinq JARs embarqués ont le même identifiant de mod `golems_companions`, avec une contrainte `minecraft` distincte. Vérifier par lancement **chacune** des versions de Minecraft et le choix effectif du module par Fabric Loader.

### P3 — Documents présents dans le JAR

Le document `INSTALLATION.md` intégré mentionne explicitement **deux distributions** : `mc1.21-1.21.11` et `mc26.1-26.3`. CurseForge présente également des fichiers par famille de versions Minecraft. Le présent audit est **celui du binaire 26.x uniquement** : l’existence du JAR 1.21.x n’autorise pas à lui attribuer les dépendances, contenus ou défauts du build 26.x sans l’avoir inspecté.

### P3 — Documentation des enchantements

Tous les enchantements ont actuellement `max_level: 1` et `effects: {}`. Les effets sont ailleurs en Java ; maintenir le guide lors des changements dans `AncientEffects`, `AncientTools`, `AncientUtility` et les mixins. Les détails et pourcentages doivent être validés dans le jeu.

## Ce qui n'a pas été testé

Le JAR n'a **pas** été exécuté sous Minecraft ; il n'y a donc pas de validation d'absence de crash, de synchronisation réseau, d’équilibrage des drops, des apparitions, ni des conflits de mods.


## Correctif documentaire effectué dans ce dépôt

Le premier brouillon classait à tort de nombreux enchantements comme applicables aux **bateaux**, à cause d'un test de sous-chaîne `raft` qui correspondait également à la fin du mot `minecraft` dans les identifiants. **Ce wiki corrige cette erreur** en analysant le nom d'objet, sans le namespace, puis en fournissant pour chaque enchantement une **liste exacte de ses objets compatibles** telle que définie dans le tag du JAR.

Cette correction porte sur la documentation préparée, pas sur le JAR du mod (dont les tags n'étaient pas erronés).
