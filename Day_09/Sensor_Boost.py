from IntCode_Machine import IntCodeMachine

# Decided to write an actual intcode machine for this challenge

code_arr = []
with open('input', 'r') as f:
    for line in f:
        code_arr = [int(num) for num in line.split(',')]
machine = IntCodeMachine(code_arr)
print(machine.run(1))
print(machine.run(2))