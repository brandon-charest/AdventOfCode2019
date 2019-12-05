import math


def calculate_fuel(mass):
    new_mass = math.floor(mass / 3) - 2
    return new_mass + calculate_fuel(new_mass) if new_mass > 0 else 0


fuel_req = 0
with open('input', 'r') as f:
    for num in f:
        fuel_req += calculate_fuel(int(num))
print(fuel_req)
