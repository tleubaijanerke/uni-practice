import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save_settings(settings):
    path = os.path.join(BASE_DIR, "settings.json")
    with open(path, "w") as f:
        json.dump(settings, f, indent=4)

def load_settings():
    path = os.path.join(BASE_DIR, "settings.json")
    default = {"sound": True, "difficulty": "medium"}
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    return default
        except:
            return default
    return default

def save_leaderboard(entries):
    path = os.path.join(BASE_DIR, "leaderboard.json")
    with open(path, "w") as f:
        json.dump(entries, f, indent=4)

def load_leaderboard():
    path = os.path.join(BASE_DIR, "leaderboard.json")
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    return []
        except:
            return []
    return []

def add_score(leaderboard, name, score, distance, coins):
    leaderboard.append({"name": name, "score": score, "distance": distance, "coins": coins})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    return leaderboard[:10]