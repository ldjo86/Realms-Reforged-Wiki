# Golems de matériaux

Le JAR fournit les apparences de golems de fer en **or, émeraude, diamant et netherite** ; chaque type possède une texture normale et trois niveaux de fissures.

Contrairement à un ajout d'entités séparées, ces variantes restent des `minecraft:iron_golem` distingués par des tags et des équipes. Cette particularité est confirmée par le fichier `INSTALLATION.md` embarqué dans l'archive.

## Aperçu des textures originales

| Or | Émeraude | Diamant | Netherite |
|---|---|---|---|
| ![Golem or](../assets/textures/golems/gold.png) | ![Golem émeraude](../assets/textures/golems/emerald.png) | ![Golem diamant](../assets/textures/golems/diamond.png) | ![Golem netherite](../assets/textures/golems/netherite.png) |

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
