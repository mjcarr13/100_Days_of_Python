import json

with open("data.json", mode="r") as data_file:
    json_data = json.load(data_file)

print(json_data["c"]["password"])