import json
import os
from aqt import mw
from datetime import datetime

# saved in the profile folder so it survives add-on updates, stays out of my repo, and each profile gets its own city
def _save_path():
    folder = mw.pm.profileFolder()
    return os.path.join(folder, "anki_city.json")

# first session ever has no file yet, so start with an empty city instead of crashing
def load_city():
    path = _save_path()
    if not os.path.exists(path):
        return {"sessions": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# loads everything first because opening with "w" replaces the whole file
def save_session(building_type, total_buildings, cards_reviewed, broken):
    data = load_city()
    data["sessions"].append({
        "building": building_type,
        "count": total_buildings,
        "broken": broken,
        "cards": cards_reviewed,
        "finished_at": datetime.now().isoformat(timespec="seconds"),
    })
    with open(_save_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)