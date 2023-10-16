# -*- coding: utf-8 -*-
"""Copy of csv to json files.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MIex5wq4NT4TyZAS49rmdkluQXrCqBAC
"""

import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Create a list to store the data
    data = []

    # Open the CSV file and read its contents
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Convert each row into a dictionary and add it to the list
        for row in csv_reader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Example usage:
csv_to_json('/content/input.csv', '/content/output.json')

import json

# Load the JSON data
with open('output.json', 'r') as f:
    data = json.load(f)

# Format the data for Elasticsearch bulk operations
formatted_data = []
for item in data:
    # Add the action metadata
    action = {
        "index": {
            "_index": "restindex",  # Replace with your index name
            "_id": item.get("id", None)  # Assuming each item has an 'id' field
        }
    }
    formatted_data.append(action)
    formatted_data.append(item)

# Save the formatted data to a new file
with open('formatted_data.json', 'w') as f:
    for line in formatted_data:
        f.write(json.dumps(line) + '\n')