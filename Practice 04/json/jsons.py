# JSON Syntax (examples)
# JSON uses:
# - double quotes for strings and keys
# - true/false/null (NOT True/False/None)
# - arrays [] and objects {}

import json 

json_text_example = """
{
  "name": "Yernar",
  "age": 19,
  "is_student": true,
  "scores": [90, 85, 100],
  "address": null
}
""".strip()

print(json_text_example)

# Parsing JSON (loads)

data_from_text = json.loads(json_text_example)  # JSON string -> Python dict
print("Python object type:", type(data_from_text))
print("Name:", data_from_text["name"])
print("Scores:", data_from_text["scores"])

# Python -> JSON (dumps)

me = {
    "name": "Yernar",
    "age": 19,
    "is_student": True,
    "skills": ["Python", "SQL", "Presentations"],
    "favorite_numbers": (7, 13),       # tuple -> JSON array
    "gpa": 3.75,                       # float
    "best_friend": None                # None -> null in JSON
}

print(json.dumps(me, indent = 2))             # dict
print(json.dumps(me["skills"]))               # list
print(json.dumps(me["favorite_numbers"]))     # tuple
print(json.dumps(me["name"]))                 # string
print(json.dumps(me["age"]))                  # int
print(json.dumps(me["gpa"]))                  # float
print(json.dumps(me["is_student"]))           # True
print(json.dumps(False))                      # False
print(json.dumps(me["best_friend"]))          # None
print(json.dumps(me, indent = 4, separators=(". ", " = ")))
print(json.dumps(me, indent = 4, sort_keys=True))
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null