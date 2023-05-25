import os
import json

def list_files(startpath):
    result = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            result.append(os.path.join(root, file))
    return result

file_list = list_files('/path/to/directory')
json_data = json.dumps(file_list)

print(json_data)