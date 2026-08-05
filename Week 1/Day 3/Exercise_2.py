import importlib.metadata

try:
    version = importlib.metadata.version("requests")
    print(f"requests is installed. Version: {version}")
except importlib.metadata.PackageNotFoundError:
    print("requests is not found.")

total = len(list(importlib.metadata.distributions()))
print(f"Total installed packages: {total}")
