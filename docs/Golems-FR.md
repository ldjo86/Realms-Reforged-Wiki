# Les golems de matériaux — capacités et fonctionnement

**Or, émeraude, diamant et Netherite** : Realms Reforged ajoute quatre variantes de golems, chacune avec des capacités propres. Leur rôle est expliqué ici comme dans un véritable guide Minecraft, sans montrer leurs textures ni leur apparence avant les photographies publiées par l'auteur.

Les variantes utilisent les entités vanilla `minecraft:iron_golem`, différenciées par les tags et les équipes du mod. Les données détaillées ci-dessous concernent le JAR **1.13.1 / Minecraft 26.x** examiné : le fonctionnement exact d'une autre compilation doit être vérifié séparément.

## Découvrir leurs capacités

| Variante | Particularité principale |
|---|---|
| **Or** | Soutien offensif plus rapide, avec bonus de vitesse et de force |
| **Émeraude** | Soin des villageois et des golems proches |
| **Diamant** | Protection et résistance renforcées |
| **Netherite** | Résistance élevée et puissants effets de combat, au prix d'une vitesse réduite |

**Choisissez votre approche :** privilégiez la protection d'un village avec un golem émeraude, ou préparez de lourds affrontements avec les variantes avancées. Les seuils précis d'apparition et les valeurs des effets figurent dans les tableaux ci-dessous.

## Apparence : à découvrir dans Minecraft

Aucune texture, UV, skin ou représentation des golems n'est distribuée par ce wiki. Les ressources originales restent dans les JAR du jeu. Le créateur ajoutera lui-même des photos aux [publications CurseForge](https://www.curseforge.com/minecraft/mc-mods/realms-reforged) lorsqu'il souhaitera dévoiler leur apparence.

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
