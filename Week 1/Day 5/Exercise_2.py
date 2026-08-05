names = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 19.99, 49.99]

print("Procedural Report (correct):")
for name, price in zip(names, prices):
    print(f"{name}: ${price}")

names.remove("Mouse")

print("Procedural Report (after desync):")
for name, price in zip(names, prices):
    print(f"{name}: ${price}")
print("Keyboard is now incorrectly shown with Mouse's price ($19.99) instead of its own ($49.99).")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"


products = [
    Product("Laptop", 999.99),
    Product("Mouse", 19.99),
    Product("Keyboard", 49.99),
]

print("OOP Report (correct):")
for product in products:
    print(product.describe())

products = [p for p in products if p.name != "Mouse"]

print("OOP Report (after clean removal):")
for product in products:
    print(product.describe())
