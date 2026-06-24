import os
import urllib.request

os.makedirs("data/full_dataset", exist_ok=True)

files = [
    "goemotions_1.csv",
    "goemotions_2.csv",
    "goemotions_3.csv"
]

base_url = "https://storage.googleapis.com/gresearch/goemotions/data/full_dataset/"

for file in files:
    print(f"Downloading {file}...")
    urllib.request.urlretrieve(
        base_url + file,
        f"data/full_dataset/{file}"
    )

print("Done!")