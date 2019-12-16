from IntCode_Machine import IntCodeMachine
from IntCode_Machine import OP_TYPE
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


def paint(code, start):
    computer = IntCodeMachine(code, mode='paint')
    image = defaultdict(int)
    x, y = 0, 0
    image[(x, y)] = start
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0

    while True:
        program_out = computer.run(image[(x, y)])
        if computer.op is OP_TYPE.HALT:
            break
        color, turn = program_out
        image[(x, y)] = color
        direction = (direction + turn * 2 - 1) % 4
        x += directions[direction][0]
        y += directions[direction][1]
    return image


code_arr = []
with open('input', 'r') as f:
    for line in f:
        code_arr = [int(i) for i in line.split(',')]

print("Painted:", len(paint(code_arr, start=0)))

image = paint(code_arr, start=1)
xs = [x for x, y in image.keys()]
ys = [y for x, y in image.keys()]
max_x = max(xs) + 1
max_y = max(ys) + 1

grid = np.zeros([max_y,max_x])
for y in range(0, max_y):
    for x in range(0, max_x):
        grid[y][x] = image[(x, y)]
plt.imshow(grid)
plt.savefig('output.png')
plt.show()

