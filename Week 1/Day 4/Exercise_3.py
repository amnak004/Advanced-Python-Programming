import random

random.seed(42)

seven_count = 0

for i in range(1, 11):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Roll {i}: {die1} + {die2} = {total}")
    if total == 7:
        seven_count += 1

print(f"Number of rolls that summed to 7: {seven_count}")
