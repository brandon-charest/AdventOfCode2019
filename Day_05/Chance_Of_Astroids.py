def decode_opcode(instruction):
    return instruction.rjust(5, '0')


def compute(arr, input=0):
    ptr = 0
    skip = [4, 4, 2, 2, 3, 3, 4]
    while arr[ptr] != 99:
        instruction = decode_opcode(str(arr[ptr]))
        opcode = int(instruction[-2:])
        op1, op2, op3 = map(int, instruction[-3:-6:-1])
        # Addition
        if opcode is 1:
            val1 = arr[ptr + 1] if op1 is 0 else ptr + 1
            val2 = arr[ptr + 2] if op2 is 0 else ptr + 2
            arr[arr[ptr + 3]] = arr[val1] + arr[val2]
        # Multiplication
        elif opcode is 2:
            val1 = arr[ptr + 1] if op1 is 0 else ptr + 1
            val2 = arr[ptr + 2] if op2 is 0 else ptr + 2
            arr[arr[ptr + 3]] = arr[val1] * arr[val2]
        # Input
        elif opcode is 3:
            arr[arr[ptr+1]] = input
        # Output
        elif opcode is 4:
            val = arr[ptr + 1] if op1 is 0 else ptr + 1
            arr[0] = arr[val]
        ptr += skip[opcode - 1]
    return arr[0]


code_arr = []
with open('input', 'r') as f:
    for line in f:
        code_arr = [int(num) for num in line.split(',')]
        print(compute(code_arr, input=1))
