# Installation / Compatibility / Installation et compatibilité

**Realms Reforged possède plusieurs JAR, chacun destiné à une famille précise de versions Minecraft. / Realms Reforged ships separate JAR families.**

| Minecraft | Distribution | Ce qui est vérifié / What is verified |
|---|---|---|
| **1.21–1.21.11** | JAR `mc1.21-1.21.11` | Le fichier `INSTALLATION.md` du mod mentionne cette famille ; [CurseForge liste notamment un build 1.13.0](https://www.curseforge.com/minecraft/mc-mods/realms-reforged/files/all). **Binaire 1.21.x non analysé ici.** / Listed but not audited here. |
| **26.1–26.3** | JAR `mc26.1-26.3` | **Build 1.13.1 examiné statiquement**. / Statically audited build. |

## Installation du JAR 1.13.1 / 26.x (seul fichier audité)

- Les métadonnées de **ce** JAR déclarent Minecraft Java **>=26.1 <=26.3**, Fabric Loader **>=0.19.5**, **Fabric API**, **Java >=25**.
- Mets **ce JAR externe unique** dans `mods` : les cinq modules `companions-26.*.jar` sont déjà intégrés.
- En multijoueur, suis les instructions client et serveur du JAR.

## Installation d'un JAR 1.21.x / Installing a 1.21.x build

- **Télécharge la distribution 1.21.x** correspondant exactement à ton Minecraft depuis [les fichiers du mod sur CurseForge](https://www.curseforge.com/minecraft/mc-mods/realms-reforged/files/all), ou utilise ton JAR local si tu en disposes.
- **N'installe jamais les deux familles de JAR en même temps.** / Never install both JAR families together.
- **Ne déduis pas les exigences Java ou Fabric de la version 26.x** : lis les dépendances et contraintes du `fabric.mod.json` contenu dans le **JAR 1.21.x**. Nous n'avons pas ce binaire à analyser. / Check that build's own metadata.

## Migration / Moving from an older datapack

Sauvegarde ton monde. Si tu remplaces l'ancien datapack Golems par un JAR, retire le ZIP correspondant pour éviter la duplication des fonctions. / Back up your world and remove the old standalone Golems datapack when migrating to the mod.

## Limites / Limitations

Il s'agit d'une inspection **statique** des archives disponibles, pas d'une validation de démarrage ou d'absence de crash. Les contraintes d'une famille ne sont pas présumées vraies pour toutes les autres versions. / Static inspection does not guarantee that a build launches on every stated Minecraft version or with all Fabric API versions.

[Liste des versions et sources / Version provenance](Version-et-provenance.md)
