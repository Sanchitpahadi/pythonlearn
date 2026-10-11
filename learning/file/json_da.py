import json

data = {"name":"Alice", "score": [91,87,79]}

with open("data.json","w") as f :
    json.dump(data, f , indent = 2)


with open("data.json","r") as f:
    loaded = json.load(f)
    print(loaded["name"])
    print(loaded["score"])

