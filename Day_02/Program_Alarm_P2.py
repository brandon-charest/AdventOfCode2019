

def compute(num1, num2, arr):
    arr[1], arr[2], m_ptr = num1, num2, 0
    while arr[m_ptr] != 99:
        current = arr[m_ptr]
        val1 = arr[arr[m_ptr + 1]]
        val2 = arr[arr[m_ptr + 2]]
        val3_idx = arr[m_ptr + 3]
        if current == 1:
            arr[val3_idx] = val1 + val2
        elif current == 2:
            arr[val3_idx] = val1 * val2
        m_ptr += 4
    return arr[0]


code_arr = []
with open('input', 'r') as f:
    for line in f:
        code_arr = [int(num) for num in line.split(',')]
target = 19690720
for i in range(100):
    for j in range(100):
        if compute(i, j, code_arr[:]) == target:
            print(100 * i + j)
            break
