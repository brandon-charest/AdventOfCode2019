import math


def calculate_fuel(mass):
    return math.floor(mass/3) - 2


fuel_req = 0
with open('input', 'r') as f:
    for num in f:
        fuel_req += calculate_fuel(int(num))
print(fuel_req)
