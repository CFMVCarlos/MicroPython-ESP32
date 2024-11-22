import json

# Example dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "age_restriction": None,
}

# Dumping the dictionary to a JSON string and writing it to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Loading the JSON string from the file and parsing it to a Python object
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Loaded data:", loaded_data)

# Dumping the dictionary to a compact JSON string
compact_json_str = json.dumps(data, separators=(",", ":"))
print("Compact JSON string:", compact_json_str)

# Parsing the JSON string to a Python object
parsed_data = json.loads(compact_json_str)
print("Parsed data:", parsed_data)
