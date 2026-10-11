# Material Golems — Gold, Emerald, Diamond and Netherite

Realms Reforged expands Minecraft's iron golem encounters with **four material variants**, each carrying different combat or support abilities. This guide focuses on gameplay, without showing their appearance. The author will reveal screenshots at their discretion on [CurseForge](https://www.curseforge.com/minecraft/mc-mods/realms-reforged).

The audited 1.13.1 / 26.x JAR implements these as `minecraft:iron_golem` variants using tags and teams rather than separate registered creature types. Behaviour on other Minecraft versions must be checked against the corresponding JAR.

## Roles at a glance

| Variant | Gameplay specialty |
|---|---|
| **Gold** | Speed and attack strength |
| **Emerald** | Healing nearby villagers and golems |
| **Diamond** | Toughness, resistance and strength |
| **Netherite** | Strong protection and attack buffs, with reduced mobility |

## Creature appearances are intentionally hidden

This wiki no longer republishes golem textures, skins or raw UV layouts. The actual assets remain available in the mod's distribution and are intended to be discovered in-game. Technical audit notes do not replace in-game validation.

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
