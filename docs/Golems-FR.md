# Golems de matériaux

Le mod comporte quatre variantes de golems de fer : **or, émeraude, diamant et Netherite**. Le JAR 1.13.1 / 26.x analysé fournit **16 chemins de textures** (une base et trois stades de fissures par matériau). **Attention : ces 16 fichiers ne contiennent que quatre images différentes**, répétées sous les quatre noms de matériaux. Cette observation concerne le JAR fourni, pas nécessairement tous les autres JAR du projet.

Contrairement à un ajout d'entités séparées, ces variantes restent des `minecraft:iron_golem` distingués par des tags et des équipes. Cette particularité est confirmée par le fichier `INSTALLATION.md` embarqué dans l'archive.

## Textures — vérification des fichiers du JAR

⚠️ **L’ancienne rangée de quatre textures distinctes était trompeuse.** Nous avons comparé les fichiers PNG extraits du **JAR 1.13.1 pour 26.1–26.3** :

| Fichiers dans `assets/golems_materiaux/textures/entity/golem/` | Résultat |
|---|---|
| `gold.png`, `emerald.png`, `diamond.png`, `netherite.png` | **Quatre fichiers strictement identiques**, 128 × 128 pixels |
| `{matériau}_crackiness_low.png` | Identiques pour les quatre matériaux |
| `{matériau}_crackiness_medium.png` | Identiques pour les quatre matériaux |
| `{matériau}_crackiness_high.png` | Identiques pour les quatre matériaux |

La classe `fr/golems/client/GolemTextures.class` sélectionne pourtant le chemin d’une variante à partir des équipes `dgp_gold`, `dgp_emerald`, `dgp_diamond` et `dgp_netherite`. **Des chemins de textures différents ne garantissent pas des pixels différents.** Cette inspection statique ne prouve pas l’apparence finale en jeu, ni celle des JAR **1.21.x** non inspectés.

**Texture témoin réellement intégrée à ce JAR** (une seule représentation, et **pas** quatre visuels prétendument différents) :

![PNG de base commun aux quatre golems dans ce JAR](../assets/textures/golems/gold.png)

Pour obtenir quatre aperçus fidèles, il faudra **récupérer les vrais PNG propres à chaque golem** depuis une autre distribution valide ou les ressources source, puis confirmer leur rendu en jeu. Les fichiers du JAR original sont conservés sans modification dans ce wiki. [Galerie et noms de fichiers](Textures-Gallery.md) · [Empreintes SHA-256 des 16 PNG](../inventory/golem-texture-sha256.json).


## Fonctionnement et données

- Fabric Loader >=0.19.5 et Fabric API nécessaires.
- Aucun pack de textures séparé ni ETF/OptiFine nécessaires pour les textures natives.
- Les fonctions de datapack historiques utilisent le namespace `dg` ; gestion de génération et rôles via les fonctions `data/dg/function/`.
- Les variantes disposent de loot tables dans `data/dg/loot_table/entities/` et d'options administrateur pour le doublement des golems naturels.
- Des soins propres aux golems émeraude apparaissent dans `dg:emerald/heal_aura` et `dg:emerald/self_heal`.

La mise en jeu réelle de chaque mécanique dépend du monde et des conditions d'exécution ; les fichiers JAR sont la source et non une validation de gameplay.


## Apparitions naturelles — règles précises

Lorsqu'un **golem naturel** est généré par Minecraft, le datapack `dg:natural/process` compte les villageois dans un rayon de **32 blocs** et choisit au hasard parmi les types débloqués.

| Villageois dans les 32 blocs | Variantes tirées au sort |
|---:|---|
| 0–5 | Fer vanilla |
| 6–8 | Fer ou or |
| 9–11 | Fer, or ou émeraude |
| 12–14 | Fer, or, émeraude ou diamant |
| 15+ | Fer, or, émeraude, diamant ou netherite |

Le fer reste dans le tirage à tous les seuils. À partir de **6 villageois**, une seconde apparition peut se produire dans le même événement de génération, à condition qu'un emplacement valide soit trouvé. **Chance par défaut : 50 %**, modifiable par les commandes administrateur. Les golems construits par le joueur au moyen de la méthode vanilla restent des golems de fer normaux dans cette logique.

## Pouvoirs des variantes — données des fonctions

| Type | Particularités visibles dans les fichiers de fonctions |
|---|---|
| **Or** | Vitesse I, Force I, vie plafonnée à 80 points |
| **Émeraude** | Aura de soin pour villageois et golems proches (10 blocs, toutes les 5 s) ; auto-soin toutes les 10 s hors dégâts |
| **Diamant** | Bonus de santé, Résistance I et Force II ; santé initialisée à 140 points dans la fonction |
| **Netherite** | Bonus de santé plus élevé, Résistance II, Force III, Lenteur I ; santé initialisée à 180 points dans la fonction |

Les **effets de potion** sont appliqués pour une très longue durée ; leur combinaison avec la santé NBT et les règles de Minecraft peut influencer la santé effective. Les valeurs doivent être contrôlées en jeu avant de promettre des maxima exacts.

## Réglages administrateur

```mcfunction
/function dg:admin/info
/function dg:admin/double_off
/function dg:admin/double_25
/function dg:admin/double_50
/function dg:admin/double_75
/function dg:admin/double_100
```

Ces fonctions changent le pourcentage de chance d'un **second** golem naturel, sans imposer une variante spécifique. Elles nécessitent les permissions de commandes nécessaires.
