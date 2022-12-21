import json
import os.path


def add_score(name, difficulty):
    score = difficulty * (3 + 5)
    new_data = {
        name: {
            "username": name,
            "score": score,
            "total": 0,
        }
    }
    data = {}
    try:
        if not os.path.getsize("score.json") == 0:
            with open("score.json", "r") as score_file:
                data = json.load(score_file)
    except FileNotFoundError:
        with open("score.json", "w") as score_file:
            json.dump(new_data, score_file, indent=2)
    else:
        if data[name]:
            data[name]["total"] += score
            data[name]["score"] = score
        else:
            data.update(new_data)
        with open("score.json", "w") as score_file:
            json.dump(data, score_file, indent=2)
