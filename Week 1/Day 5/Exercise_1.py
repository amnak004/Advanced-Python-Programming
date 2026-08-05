def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


class TemperatureReading:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


celsius_value = 25

procedural_result = celsius_to_fahrenheit(celsius_value)
print(f"Procedural result: {celsius_value}C = {procedural_result}F")

reading = TemperatureReading(celsius_value)
oop_result = reading.to_fahrenheit()
print(f"OOP result: {celsius_value}C = {oop_result}F")
