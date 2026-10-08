# Installation / Compatibility

**Verified from JAR metadata — Golems de matériaux v1.13.1**

- Minecraft Java Edition **26.1, 26.1.1, 26.1.2, 26.2, 26.3**.
- Fabric Loader **0.19.5 or newer**.
- Matching **Fabric API**.
- **Java 25 or newer**.
- Install **one outer JAR only**; the five internal version-specific `golems_companions` modules are already bundled.
- For multiplayer, install the mod/Fabric API on the server and clients (visual rendering is client-side).

## Moving from an old datapack

Make a world backup. Remove the previous Golems datapack ZIP before installing this mod so its functions do not run twice. The older `dg` commands, scores and team identifiers are intended to be retained. See the `INSTALLATION.md` inside the JAR.

## Important limitations

This is static archive verification. It does **not** certify startup success or compatibility with every Fabric API/build. The review machine has Java 21, whereas the bundled `golems_companions` classes require Java 25 (class-file major 69); runtime tests must use a suitable JDK.
