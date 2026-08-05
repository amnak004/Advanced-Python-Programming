import sys
import os
import platform

print(f"Executable Path: {sys.executable}")
print(f"Python Version: {platform.python_version()}")
print(f"Working Directory: {os.getcwd()}")
print(f"Search Path Entries: {len(sys.path)}")
