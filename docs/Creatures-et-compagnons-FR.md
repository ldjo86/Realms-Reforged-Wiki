# Créatures, boss et compagnons

Le module Java compagnon `golems_companions` est intégré dans le JAR. Les entités listées ci-dessous apparaissent explicitement dans les routines d'enregistrement (`CustomEntities`).

| Identifiant | Texture originale / information |
|---|---|
| `illageois_demi_squelette` | ![illageois_demi_squelette](../assets/textures/creatures/illageois_demi_squelette.png) |
| `illageois_zombifie` | ![illageois_zombifie](../assets/textures/creatures/illageois_zombifie.png) |
| `demon_commandant` | ![demon_commandant](../assets/textures/creatures/demon_commandant.png) |
| `goule` | ![goule](../assets/textures/creatures/goule.png) |
| `illageois_gueri` | ![illageois_gueri](../assets/textures/creatures/illageois_gueri.png) |
| `maitre_squelette` | ![maitre_squelette](../assets/textures/creatures/maitre_squelette.png) |
| `maitre_des_zombies` | ![maitre_des_zombies](../assets/textures/creatures/maitre_des_zombies.png) |
| `maitre_creeper` | ![maitre_creeper](../assets/textures/creatures/maitre_creeper.png) |

## Sous-systèmes présents

- Alliés illageois (`FriendlyIllager`), professions (`ExtraProfessions`, `IllagerCareer`), échanges (`IllagerTrades`) et réputation (`IllagerReputation`).
- Golems compagnons avec rôles (`CompanionGolem`, `CompanionRoles`).
- Commandement et groupe (`LeaderOrders`, `LeaderRoster`, `CompassPatrol`).
- Créatures hostiles et boss (`MasterMobs`, `MiniBosses`, `VanillaMiniBosses`, `CreatureSpawns`).
- Soin, équipements, trophées et butin (`HealingStandard`, `IllagerEquipment`, `HostileDrops`, `MasterTrophyBlock`).

**Attention :** cette page confirme la présence des mécanismes et des entités. L'apparition effective, les conditions exactes et les probabilités nécessitent un test de partie.


## Fonctionnement annoncé sur CurseForge

Les **Illageois zombifiés** peuvent être guéris par **Faiblesse + pomme dorée**, avec une durée annoncée d'environ **3 à 5 minutes**. L'**Élixir doré** et sa version jetable constituent une autre méthode. Les Illageois guéris deviennent des alliés personnalisables : armes, boucliers, arbalètes, professions, gardes postés avec des bannières et ordres de suivi.

Les rôles de golems compagnons indiqués par le projet sont **Éclaireur**, **Soigneur**, **Protecteur**, **Combattant lourd** et **Gardien**. Le système des **trois Maîtres** concerne le Maître squelette, le Maître zombie et le Maître creeper. Des mini-boss tels que la **Goule géante**, le **Champion zombifié** et le **Champion demi-squelette** sont également annoncés.

Détails précis d'apparition, de dégâts et de taux de butin : **à tester en partie**.
