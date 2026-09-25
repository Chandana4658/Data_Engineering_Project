import json
from pathlib import Path

print("================================")
print(" DATA ENGINEERING DOCKER APP")
print("================================")

data_file = Path("/app/data/users.json")

if data_file.exists():

    with open(data_file, "r") as file:
        data = json.load(file)

    print(f"Records processed: {len(data)}")

else:
    print("users.json not found")