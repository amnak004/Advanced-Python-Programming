values = ["hello", [1, 2, 3], 42, 3.14, True]

for value in values:
    print(f"Value: {value}")
    print(f"Type: {type(value)}")
    print(f"isinstance(value, int): {isinstance(value, int)}")
    try:
        print(f"Length: {len(value)}")
    except TypeError:
        print("Length: no length")
    print()
