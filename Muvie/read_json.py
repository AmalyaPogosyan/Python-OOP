import json
PATH = "imdb_top_999.json"

with open(PATH, "r") as f:
    data = json.load(f)

TO_DELETE = ["No_of_Votes", "Overview", "Meta_score"]

for kino in data.keys():
    for k in TO_DELETE:
        del data[kino][k]

    data[kino]["Name"] = kino
