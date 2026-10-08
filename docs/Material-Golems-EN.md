# Material Golems — Gold, Emerald, Diamond and Netherite

Realms Reforged has four iron-golem material variants (gold, emerald, diamond and netherite). The audited 1.13.1 / 26.x JAR contains **16 named texture paths**, but only **four distinct PNG image contents**: one shared base skin and three shared crack stages. The same conclusion must **not** be assumed for unexamined 1.21.x builds. These are variants of `minecraft:iron_golem` controlled by the `dg` datapack with tags and teams, **not four separately registered entity types**.

## Texture verification — important

⚠️ **The four preview images previously shown here were misleading.** Byte-for-byte comparison of the audited JAR demonstrates that:

| Packaged PNGs | Result |
|---|---|
| `gold.png`, `emerald.png`, `diamond.png`, `netherite.png` | **All four identical**, 128 × 128 pixels |
| `*_crackiness_low.png` | Identical across all four materials |
| `*_crackiness_medium.png` | Identical across all four materials |
| `*_crackiness_high.png` | Identical across all four materials |

The class `fr/golems/client/GolemTextures.class` chooses a texture path based on teams named `dgp_gold`, `dgp_emerald`, `dgp_diamond` and `dgp_netherite`; however, **distinct paths do not guarantee visually distinct source textures**. These static files alone cannot confirm the final in-game appearance or the appearance in other JAR versions.

**One representative raw base PNG** from this exact JAR (not a 3D gameplay render):

![Shared golem base PNG in the audited archive](../assets/textures/golems/gold.png)

We will replace this placeholder preview **only after inspecting authentic distinct textures from another verified build or original assets**. The packaged source images themselves are retained unchanged. [Texture gallery](Textures-Gallery-EN.md) · [SHA-256 inventory of all 16 PNGs](../inventory/golem-texture-sha256.json).


## Natural generation

When Minecraft naturally generates an iron golem, the mod counts villagers in a **32-block radius**:

| Nearby villagers | Variants eligible in the random selection |
|---:|---|
| 0–5 | Regular iron |
| 6–8 | Iron, gold |
| 9–11 | Iron, gold, emerald |
| 12–14 | Iron, gold, emerald, diamond |
| 15+ | Iron, gold, emerald, diamond, netherite |

Regular iron always remains an option. With **at least 6 villagers**, the same spawn event can produce a second golem if there is safe space; default chance is **50%**. Player-built vanilla golems stay regular iron golems under the datapack’s natural-spawn selection rules.

## Distinct abilities in the packaged functions

| Type | Effects |
|---|---|
| Gold | Speed I, Strength I; health clamped at 80 points by the tick function |
| Emerald | Heals nearby villagers and golems up to 10 blocks every 5 seconds, and heals itself out of combat every 10 seconds |
| Diamond | Health Boost, Resistance I, Strength II; sets health to 140 in its variant function |
| Netherite | Stronger Health Boost, Resistance II, Strength III, Slowness I; sets health to 180 in its variant function |

Effect-based maximum health needs live testing to confirm exact runtime totals.

## Administrator controls

```mcfunction
/function dg:admin/info
/function dg:admin/double_off
/function dg:admin/double_25
/function dg:admin/double_50
/function dg:admin/double_75
/function dg:admin/double_100
```

These change the chance of a **second natural golem**, not which variant is chosen. See [installation and requirements](Installation-Compatibility.md).
