
class Intcode:
    def __init__(self):
        self.m_ptr = 0

    def compute(self, arr):
        # restore code arr to position before crash
        arr[1] = 12
        arr[2] = 2

        while arr[self.m_ptr] is not 99:
            if arr[self.m_ptr] is 1:
                arr[arr[self.m_ptr + 3]] = arr[arr[self.m_ptr + 1]] + arr[arr[self.m_ptr + 2]]
            elif arr[self.m_ptr] is 2:
                arr[arr[self.m_ptr + 3]] = arr[arr[self.m_ptr + 1]] * arr[arr[self.m_ptr + 2]]
            self._forward()
        return arr

    def _forward(self):
        self.m_ptr += 4


code_arr = []
with open('input', 'r') as f:
    for line in f:
        code_arr = [int(num) for num in line.split(',')]


intcode = Intcode()
print(intcode.compute(code_arr))