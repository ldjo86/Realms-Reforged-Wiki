# Version coverage & provenance

> This wiki audits **the user-supplied `golems-materiaux-1.13.1-mc26.1-26.3-fabric.jar`**. The public CurseForge page observed on October 8, 2026 lists a **1.13.0** release. Do not confuse the audited candidate with the currently listed downloadable release.

Public project name: **Realms Reforged**. Main JAR metadata: `golems_materiaux`, nested modules: `golems_companions`.

| Embedded module | Minecraft constraint | Mod version | Java |
|---|---|---|---|
| `companions-26.1.1.jar` | `26.1.1` | `1.13.1+26.1.1` | `>=25` |
| `companions-26.1.2.jar` | `26.1.2` | `1.13.1+26.1.2` | `>=25` |
| `companions-26.1.jar` | `26.1` | `1.13.1+26.1` | `>=25` |
| `companions-26.2.jar` | `26.2` | `1.13.1+26.2` | `>=25` |
| `companions-26.3.jar` | `26.3` | `1.13.1+26.3` | `>=25` |

Five embedded JARs are included inside the **one outer JAR**, not five files to install separately. This archive requires Fabric Loader >=0.19.5, Fabric API for the game version, Java >=25 and Minecraft 26.1–26.3 according to its metadata. The older 1.21.x variant mentioned by INSTALLATION.md is a **different binary** not included here.

See [technical audit](AUDIT-technique-FR.md) and [compatibility guide](Installation-Compatibility.md).
