import json
import re

# Read in the file and the dictionary
with open('../../data/headlines.txt', 'r') as file:
    file_contents = file.read()

with open('../dictionary.csv', 'r') as dict_file:
    dict_contents = dict_file.read()

# Convert the dictionary contents to a dictionary object
dictionary = {}
for line in dict_contents.splitlines():
    key, value = line.split(',')
    dictionary[key] = value.strip()

output = []

for text in file_contents.splitlines():
    line = {}
    value = {}
    line["data"] = {}
    line["data"]["text"] = text
    line["annotations"] = []
    line["annotations"].append({"result": []})
    for key, ner in dictionary.items():
        test = key.casefold()
        string = text.casefold()
        if test in string:
            start = string.index(test)
            end = start + len(test)
            value = {"value": {"start": start, "end": end, "text": key, "labels": [ner]}, "from_name": "label", "to_name": "text", "type": "labels", "origin": "manual"}
            if len(value):
                result =  line["annotations"][0]["result"].append(value)

    output.append(line)

print(json.dumps(output, indent=2))