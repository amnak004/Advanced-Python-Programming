import math

radius = 3.7

volume = (4 / 3) * math.pi * radius ** 3
surface_area = 4 * math.pi * radius ** 2

print(f"Raw Volume: {volume:.4f}")
print(f"Raw Surface Area: {surface_area:.4f}")
print(f"Floored Volume: {math.floor(volume)}")
print(f"Ceiled Volume: {math.ceil(volume)}")
print(f"Floored Surface Area: {math.floor(surface_area)}")
print(f"Ceiled Surface Area: {math.ceil(surface_area)}")
