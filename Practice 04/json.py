# JSON Syntax (examples)
# JSON uses:
# - double quotes for strings and keys
# - true/false/null (NOT True/False/None)
# - arrays [] and objects {}

import json
from pathlib import Path


json_text_example = """
{
  "name": "Yernar",
  "age": 19,
  "is_student": true,
  "scores": [90, 85, 100],
  "address": null
}
""".strip()

print("=== 1) JSON Syntax Example (string) ===")
print(json_text_example)
print()

# Parsing JSON (loads)

data_from_text = json.loads(json_text_example)  # JSON string -> Python dict
print("Python object type:", type(data_from_text))
print("Name:", data_from_text["name"])
print("Scores:", data_from_text["scores"])
print()


# Python -> JSON (dumps)

python_obj = {
    "course": "Python",
    "topics": ["json", "files", "iterators"],
    "active": True,
    "count": 3
}

json_string = json.dumps(python_obj, ensure_ascii=False, indent=2)  # dict -> JSON string
print(json_string)
print()


# 4) Writing JSON Files

out_path = Path("output.json")
with out_path.open("w", encoding="utf-8") as f:
    json.dump(python_obj, f, ensure_ascii=False, indent=2)  # write JSON directly to file
print(f"Wrote file: {out_path.resolve()}")
print()

# 5) Reading JSON Files

with out_path.open("r", encoding="utf-8") as f:
    loaded_obj = json.load(f)  # file -> Python dict
print("Loaded:", loaded_obj)


# Working with JSON data (sample-data.json)

sample_path = Path("sample-data.json")

# If the file doesn't exist in your folder, we create a small demo version
if not sample_path.exists():
    demo_sample = [
        {"id": 1, "name": "Yernar", "age": 17, "city": "Almaty", "grades": [90, 88, 95]},
        {"id": 2, "name": "Mahambet", "age": 16, "city": "Astana", "grades": [70, 80, 75]},
        {"id": 3, "name": "Aisana", "age": 18, "city": "Almaty", "grades": [100, 98, 99]}
    ]
    with sample_path.open("w", encoding="utf-8") as f:
        json.dump(demo_sample, f, ensure_ascii=False, indent=2)
    print("sample-data.json was not found, so I created a demo sample-data.json")

# Read the sample file
with sample_path.open("r", encoding="utf-8") as f:
    sample_data = json.load(f)

print("Type of sample_data:", type(sample_data))
print("Number of records:", len(sample_data))

# Example operations (typical “work with JSON” tasks)
# Print all names
names = [item.get("name") for item in sample_data]
print("All names:", names)

# Filter: people from Almaty
almaty_people = [item for item in sample_data if item.get("city") == "Almaty"]
print("People from Almaty:", [p["name"] for p in almaty_people])

# Compute average grade for each person (if grades exist)
def avg(nums):
    return sum(nums) / len(nums) if nums else 0

averages = {item["name"]: avg(item.get("grades", [])) for item in sample_data}
print("Average grades:", averages)

# Find the person with the highest average grade
best_name = max(averages, key=averages.get) if averages else None
print("Best student by average:", best_name, "->", averages.get(best_name))