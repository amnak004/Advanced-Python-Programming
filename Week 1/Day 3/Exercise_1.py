import sys

in_venv = sys.prefix != sys.base_prefix

if in_venv:
    print("Running inside a virtual environment.")
    print(f"Environment path: {sys.prefix}")
else:
    print("Not running inside a virtual environment.")
    print(f"Base interpreter path: {sys.base_prefix}")
