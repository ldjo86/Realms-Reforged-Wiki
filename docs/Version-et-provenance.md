# Versions de Realms Reforged / Version coverage and provenance

**Le mod existe en plusieurs distributions JAR. / The project has multiple, separate JAR distributions.**

| Famille Minecraft / Minecraft family | Fichier / JAR family | État de vérification / Evidence level |
|---|---|---|
| **1.21 à 1.21.11** | `mc1.21-1.21.11` | **Mentionné par `INSTALLATION.md` à l'intérieur du JAR fourni**, et [distribution 1.13.0 visible sur CurseForge](https://www.curseforge.com/minecraft/mc-mods/realms-reforged/files/all). Le JAR **1.21.x n'a pas été fourni ici et n'a pas été audité** : exigences Java, détails fonctionnels, modèles et textures à vérifier séparément. / Referenced and publicly listed, but not audited here. |
| **26.1 à 26.3** | `golems-materiaux-1.13.1-mc26.1-26.3-fabric.jar` | **JAR fourni et analysé statiquement** : métadonnées Fabric, ressources et modules intégrés. Sans validation de lancement pour chaque sous-version. / Supplied and statically audited; no per-version startup validation. |

**Ne pas confondre la version du mod (`1.13.0`, `1.13.1`, etc.) et la version de Minecraft (`1.21.11`, `26.3`, etc.).** Les ressources et capacités peuvent différer d'un JAR à l'autre : une fiche de ce wiki établie d'après le sous-module 26.3 ne constitue pas automatiquement une preuve pour Minecraft 1.21.x. / Do not extrapolate 26.3 findings to the unexamined 1.21.x build.

## Métadonnées confirmées pour **le JAR 1.13.1 / 26.x uniquement**

- Identifiant principal : `golems_materiaux` ; module embarqué : `golems_companions`.
- Loader : Fabric Loader `>=0.19.5` ; Fabric API requise pour la version cible.
- Java : `>=25` **pour ce JAR**. Ne pas généraliser aux JAR 1.21.x sans lecture de leur `fabric.mod.json`.
- Contrainte de Minecraft déclarée par le JAR principal : `>=26.1 <=26.3`.
- Un seul **JAR externe** est installé. Les cinq modules suivants sont **inclus** dans l'archive, ils ne sont pas à installer individuellement.

| Module inclus / Bundled module | Cible Minecraft déclarée | Version du module | Java déclaré |
|---|---|---|---|
| `companions-26.1.jar` | `26.1` | `1.13.1+26.1` | `>=25` |
| `companions-26.1.1.jar` | `26.1.1` | `1.13.1+26.1.1` | `>=25` |
| `companions-26.1.2.jar` | `26.1.2` | `1.13.1+26.1.2` | `>=25` |
| `companions-26.2.jar` | `26.2` | `1.13.1+26.2` | `>=25` |
| `companions-26.3.jar` | `26.3` | `1.13.1+26.3` | `>=25` |

## Pourquoi cette prudence ? / Why this distinction matters

Le **JAR original 26.x** contient quatre familles de textures de golems mais les PNG des quatre matériaux sont **identiques par stade**. Cela n'autorise pas à affirmer que les golems paraissent identiques dans **toutes les versions**, ni que le JAR 1.21.x dispose des mêmes images. Voir [l'audit des textures FR](Golems-FR.md#textures--vérification-des-fichiers-du-jar) / [EN](Material-Golems-EN.md#texture-verification--important).

Aucune analyse de JAR ne remplace des essais en jeu pour chaque version de Minecraft. / A static JAR analysis is not a runtime compatibility certification.

[Guide d'installation / Installation guide](Installation-Compatibility.md) · [Audit technique (FR)](AUDIT-technique-FR.md) · [CurseForge : fichiers](https://www.curseforge.com/minecraft/mc-mods/realms-reforged/files/all)
