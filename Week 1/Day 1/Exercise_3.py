import dis

def multiply(a, b):
    return a * b


def is_even(number):
    return number % 2 == 0


print("=== Bytecode for multiply() ===")
dis.dis(multiply)

print("\n=== Bytecode for is_even() ===")
dis.dis(is_even)
