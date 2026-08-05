import importlib

packages_to_check = [
    ("os", "os"),
    ("sys", "sys"),
    ("requests", "requests"),
    ("beautifulsoup4", "bs4"),
    ("nonexistentpkg123", "nonexistentpkg123"),
]

missing = []

for display_name, import_name in packages_to_check:
    try:
        importlib.import_module(import_name)
        print(f"{display_name}: installed")
    except ImportError:
        print(f"{display_name}: missing")
        missing.append(display_name)

if missing:
    print("pip install " + " ".join(missing))
else:
    print("All dependencies satisfied.")
