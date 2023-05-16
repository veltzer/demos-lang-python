from typing import Dict, List

places: Dict[str, Dict[str, str]] = {
    "Shire": {"leave": "Bree", "stay": "DEATH"},
    "DEATH": {},
    "Bree": {"with Strider": "Rivendell", "alone": "DEATH"},
    "Rivendell": {"over mountains": "DEATH", "through Moria": "Lorien"},
    "Lorien": {"down Anduin": "Falls of Rauros"},
    "Falls of Rauros": {"down Anduin": "Minas Tirith",
                        "east": "Ithilien"},
    "Ithilien": {"south": "Black Gate"},
    "Black Gate": {"in": "DEATH", "follow Gollum": "Minas Morgul"},
    "Minas Morgul": {"road": "DEATH", "tunnel": "Mordor"},
    "Mordor": {"eagles": "Minas Tirith"},
    "Minas Tirith": {"return home": "Shire (tired)"},
    "Shire (tired)": {"stay": "Shire (tired)", "retire": "the West"},
    "the West": {}
}

# Only checking reachability:

reachable = {"Rivendell"}
for i in range(7):
    for place in list(reachable):
        reachable.update(places[place].values())

print("Mordor" in reachable)

# Finding the actual path:

way_to: Dict[str, List[str]] = {"Rivendell": []}
for _ in range(7):
    for place, way_to_place in way_to.items():
        for action, place2 in places[place].items():
            # If we already knew a way to place2, the new way must be longer.
            # So only set ways to places that were previously unreachable.
            if place2 not in way_to:
                way_to[place2] = way_to_place + [action]

print(way_to["Mordor"])
