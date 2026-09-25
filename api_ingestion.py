import requests
import json
from pathlib import Path

API_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_FILE = Path("data/landing/users.json")


def fetch_users():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def save_data(data):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w") as file:
        json.dump(data, file, indent=4)


def main():
    print("Starting API ingestion...")

    data = fetch_users()

    save_data(data)

    print(f"Downloaded {len(data)} records")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()