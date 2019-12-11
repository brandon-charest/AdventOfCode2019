from itertools import permutations

def decode_opcode(instruction):
    return instruction.rjust(5, '0')


def compute(arr, input, feedback=False):
    ptr = 0
    skip = [4, 4, 2, 2, 3, 3, 4, 4]
    output = -1
    while arr[ptr] != 99:
        instruction = decode_opcode(str(arr[ptr]))
        opcode = int(instruction[-2:])
        op1, op2, op3 = map(int, instruction[-3:-6:-1])
        # Addition
        if opcode is 1:
            val1 = arr[ptr + 1] if op1 is 0 else ptr + 1
            val2 = arr[ptr + 2] if op2 is 0 else ptr + 2
            arr[arr[ptr + 3]] = arr[val1] + arr[val2]
            ptr += skip[opcode - 1]
        # Multiplication
        elif opcode is 2:
            val1 = arr[ptr + 1] if op1 is 0 else ptr + 1
            val2 = arr[ptr + 2] if op2 is 0 else ptr + 2
            arr[arr[ptr + 3]] = arr[val1] * arr[val2]
            ptr += skip[opcode - 1]
        # Input
        elif opcode is 3:
            arr[arr[ptr+1]] = input.pop(0)
            ptr += skip[opcode - 1]
        # Output
        elif opcode is 4:
            val = arr[ptr + 1] if op1 is 0 else ptr + 1
            output = arr[val]
            ptr += skip[opcode - 1]
        # Jump If True
        elif opcode is 5:
            val1 = arr[ptr + 1] if op1 == 0 else ptr + 1
            if arr[val1] is not 0:
                val2 = arr[ptr + 2] if op2 == 0 else ptr + 2
                ptr = arr[val2]
            else:
                ptr += skip[opcode - 1]
        # Jump If False
        elif opcode is 6:
            val1 = arr[ptr + 1] if op1 == 0 else ptr + 1
            if arr[val1] is 0:
                val2 = arr[ptr + 2] if op2 == 0 else ptr + 2
                ptr = arr[val2]
            else:
                ptr += skip[opcode - 1]
        # Less than
        elif opcode is 7:
            val1 = arr[ptr + 1] if op1 == 0 else ptr + 1
            val2 = arr[ptr + 2] if op2 == 0 else ptr + 2
            arr[arr[ptr + 3]] = 1 if arr[val1] < arr[val2] else 0
            ptr += skip[opcode - 1]
        # Equals
        elif opcode is 8:
            val1 = arr[ptr + 1] if op1 == 0 else ptr + 1
            val2 = arr[ptr + 2] if op2 == 0 else ptr + 2
            arr[arr[ptr + 3]] = 1 if arr[val1] == arr[val2] else 0
            ptr += skip[opcode - 1]
        else:
            return print(f"Unknown Opcode:{opcode}")
    return output


code_arr = []
with open('input', 'r') as f:
    for line in f:
        code_arr = [int(num) for num in line.split(',')]

sequences = list(permutations([0,1,2,3,4]))
max_thrust = 0
for sequence in sequences:
    output = 0
    for num in sequence:
        output = compute(code_arr, [num, output])
        max_thrust = max(max_thrust, output)
print(max_thrust)

