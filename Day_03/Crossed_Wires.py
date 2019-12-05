directions = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}


def wire_points(wire):
    x, y, length = 0, 0, 0
    pts = {}
    for w in wire:
        d = directions[w[0]]
        for _ in range(int(w[1:])):
            x += d[0]
            y += d[1]
            length += 1
            pts[(x, y)] = length
    return pts


def closest_intersection(wire_data):
    wire1, wire2 = [x.split(',') for x in wire_data.split('\n')]
    wire1_pts = wire_points(wire1)
    wire2_pts = wire_points(wire2)
    cross = set(wire1_pts.keys()) & set(wire2_pts.keys())
    dist = []
    for c in cross:
        dist.append(abs(c[0]) + abs(c[1]))
    print(min(dist))


with open('input', 'r') as f:
    input_data = f.read()
    closest_intersection(input_data)



