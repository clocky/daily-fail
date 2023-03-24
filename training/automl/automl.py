import json

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


for text_content in file_contents.splitlines():
    line = {}
    text_segment_annotations = []
    for key, ner in dictionary.items():
        if key in text_content:
            start_offset = text_content.index(key)
            end_offset = start_offset + len(key) - 1
            text_segment_annotations.append({"startOffset": start_offset, "endOffset": end_offset, "displayName": ner})
    if len(text_segment_annotations):
        line["textSegmentAnnotations"] = text_segment_annotations
        line["textContent"] = text_content
        
        print(json.dumps(line))