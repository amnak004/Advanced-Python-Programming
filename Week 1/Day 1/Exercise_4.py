import os
import sys
import importlib

with open("sample_module.py", "w") as file:
    file.write("PI = 3.14\n")
    file.write("def greet():\n")
    file.write("    return 'Hello from sample module!'\n")

print("Module created successfully.")

sys.path.insert(0, os.getcwd())

import sample_module
importlib.reload(sample_module)

print("Module imported successfully.")
print(sample_module.greet())

cache_dir = "__pycache__"

if os.path.isdir(cache_dir):
    pyc_files = [file for file in os.listdir(cache_dir) if file.endswith(".pyc")]

    if pyc_files:
        print("Cache file found:", pyc_files[0])
    else:
        print("No .pyc file found.")
else:
    print("No __pycache__ directory found.")
