import os
import subprocess
from PyPDF2 import PdfMerger
import os
import json


def list_files(startpath):
    result = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            result.append(os.path.join(root, file))
    return result


file_list = list_files(".")
json_data = json.dumps(file_list)


absolute_paths = [os.path.abspath(path) for path in file_list]

for path in absolute_paths:
    print(path)
