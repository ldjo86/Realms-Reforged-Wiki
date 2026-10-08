# Contrats de chasse — guide FR

Le JAR embarque un système de chasse/prime avec plusieurs rangs, des vagues d'ennemis, des récompenses et des objectifs secondaires. Ce système n'est pas limité au simple combat contre un boss.

## Cinq structures de repaire (JAR 26.3)

| Repère | Structure | Référence incluse |
|---|---|---|
| 1 | Ruines infestées | `data/golems_materiaux/structure/hunts/ruins.nbt` |
| 2 | Hameau abandonné | `.../hunts/hamlet.nbt` |
| 3 | Grotte souterraine | `.../hunts/cave.nbt` |
| 4 | Forteresse | `.../hunts/fortress.nbt` |
| 5 | Nécropole | `.../hunts/necropolis.nbt` |

Un sixième intitulé de rang apparaît dans les traductions : **« Le conseil des trois Maîtres »**. Il ne correspond pas à un sixième fichier de structure indépendant dans l'archive.

## Parcours documenté dans les textes du mod

1. Parler à un **Chasseur de primes** et sélectionner le contrat (acceptation gratuite).
2. Récupérer la carte avec les coordonnées du repaire.
3. Nettoyer les vagues ennemies, récupérer le coffre scellé et le butin.
4. Ramener le coffre au Chasseur de primes pour toucher la prime.
5. Objectifs secondaires possibles : libérer un prisonnier, récupérer une relique ou empêcher un chef de s'enfuir.

Le système interdit les contrats en mode Paisible et en dehors de l'Overworld. Les messages intégrés indiquent qu'une fuite ou la mort peut entraîner la perte de la prime, sans empêcher toute récupération de butin.

**Attention au gameplay :** la traduction annonce que certaines chasses peuvent forcer la nuit tant que dure le combat ; à valider dans une partie avant publication définitive.


## Progression des six rangs

La page CurseForge annonce **six rangs** : ruines infestées, hameau occupé, grotte des prédateurs, forteresse d'élite, nécropole des profondeurs, puis **Conseil des trois Maîtres**. Les cinq premiers disposent d'un fichier de structure indépendant dans le sous-module 26.3 ; le rang 6 est une confrontation finale sans sixième fichier de structure `hunts/*.nbt` distinct.

Le système contient aussi des **vagues successives**, des objectifs bonus (prisonnier, relique, chef fugitif), un **coffre de prime scellé**, des récompenses sous forme de minerais/émeraudes et de fioles d'expérience. Quitter la zone ou mourir peut supprimer la prime. Les récompenses exactes dépendent du rang et du déroulement.

Voir [Professions](Professions-FR.md) pour le Chasseur de primes.
