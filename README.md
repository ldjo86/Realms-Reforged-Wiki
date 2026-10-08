# 🌍 Realms Reforged — Official Mod Wiki / Wiki du mod

[**🇫🇷 Français**](README.fr.md) | **🇬🇧 English** | [CurseForge: Realms Reforged](https://www.curseforge.com/minecraft/mc-mods/realms-reforged)

> **Project versions:** separate Minecraft 1.21–1.21.11 and 26.1–26.3 JAR families • **Technical audit:** the supplied 1.13.1 / 26.x JAR only • **Loader:** Fabric • **Status:** archive-derived, in-game checks pending.

**Realms Reforged** is a broad Minecraft expansion focused on material golems, companions and cured Illagers, new professions, enemy factions, boss encounters, bounty hunts, structures, advanced equipment, golden forests and 72 custom enchantments. The project is called **Realms Reforged on CurseForge**, while the distributed JAR uses the internal name `golems-materiaux` (`golems_materiaux` mod id) and includes a `golems_companions` module.

> **Golem artwork note:** the four base PNGs bundled in the **audited 1.13.1 / 26.x JAR** are byte-for-byte identical, as are the corresponding crack overlays at each damage level. The previously displayed four previews therefore did **not** show distinct material skins. See the [texture verification](docs/Material-Golems-EN.md#texture-verification--important). The appearance in-game and other JAR releases still require verification.

## 📖 Main wiki sections

| Topic | What's inside |
|---|---|
| 🚀 [Getting started](docs/Getting-Started-EN.md) | Installation, requirements, first steps and FAQ |
| ✨ [All 72 enchantments](docs/Enchantments-EN.md) | What they do; correct compatible items; one full page per enchantment |
| 🗿 [Four Material Golems](docs/Material-Golems-EN.md) | Gold, emerald, diamond and netherite golems; spawning, healing and admin settings |
| 🤝 [Companions, Illagers & bosses](docs/Companions-and-Creatures-EN.md) | Curing, allies, equipment, leadership, hostile creatures and Masters |
| 🧑‍🏭 [11 professions](docs/Professions-EN.md) | Advertised trades and career families |
| 🏹 [Bounty contracts](docs/Bounty-Hunts-EN.md) | Six hunt ranks, five structures, enemy waves and rewards |
| 🌳 [Golden Trees & world](docs/Golden-Trees-and-World-EN.md) | New tree generation, flowers and wooden building blocks |
| 🪦 [Graves & utilities](docs/Death-and-Utilities-EN.md) | Gravestones, Healing Standard, Diamond Anvil and special tools |
| 🛠️ [44 complete recipes](docs/Recipes-EN.md) | Materials, crafting patterns, smithing and furnace recipes |
| 📦 [Items & blocks](docs/Items-index-EN.md) | Official translated names and registry IDs |
| 🧪 [Compatibility changes](docs/Vanilla-overrides-EN.md) | 110 vanilla-namespaced recipes and leaf loot tables |
| 🎨 [82 original textures](docs/Textures-Gallery-EN.md) | Included golem, mob, item and block PNG assets |
| 🔎 [Version provenance](docs/Version-et-provenance.md) | Exact source JAR and nested Fabric modules |
| 🧾 [Technical audit (FR)](docs/AUDIT-technique-FR.md) | Method, static validation and known limitations |

## ⚙️ Installation

1. Pick the **JAR for your exact Minecraft version**: the project has separate `mc1.21-1.21.11` and `mc26.1-26.3` builds; do **not** install both together.
2. **Only the audited 1.13.1 / 26.x JAR** declares Fabric Loader 0.19.5+, the matching Fabric API and Java 25+. Check each **1.21.x JAR’s own metadata** before applying those requirements.
3. Place the selected JAR in `.minecraft/mods` and follow its multiplayer installation requirements.
4. Make a world backup and remove any previous standalone Golems datapack to avoid duplicated mechanics.

**Version note:** the audited archive is `golems-materiaux-1.13.1-mc26.1-26.3-fabric.jar`. The bundled `INSTALLATION.md` also mentions a **separate Minecraft 1.21–1.21.11 build**, and [CurseForge’s file list](https://www.curseforge.com/minecraft/mc-mods/realms-reforged/files/all) shows published builds by Minecraft version. **Do not extrapolate 26.x audit findings, Java requirements, or gameplay behavior to 1.21.x without analysing its JAR.** [Version coverage](docs/Version-et-provenance.md).

## 🧾 Evidence and limitations

Every one of the 72 enchantments and 44 custom recipes is traceable to the JAR: see [machine-readable enchantment inventory](inventory/enchantments-verified-from-jar.json) and [recipe inventory](inventory/recipes-verified-from-jar.json). Some effects are implemented in Java rather than the enchantment JSON. **Static extraction is not proof of in-game balance, multiplayer stability, loot probabilities or mod compatibility.** No original source code or JAR binary is republished here; the PNG files come directly from the supplied mod assets.

## 📢 For CurseForge visitors

If you found an unrelated or outdated wiki link, **this repository is the intended documentation for Realms Reforged**, not for another mod. The author is updating the guide in parallel with further development.

**Project:** [Realms Reforged on CurseForge](https://www.curseforge.com/minecraft/mc-mods/realms-reforged) · **License displayed on CurseForge:** All Rights Reserved. Images, names and excerpts of assets remain subject to the original project's terms.
