import math
def get_distance(p1, p2):
    return math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2))

def los(astroids, a1, a2):
    d1 = get_distance(a1, a2)
    for a3 in astroids:
        if a3 == a1:
            continue
        if a3 == a2:
            continue

        d2 = get_distance(a1, a3)
        d3 = get_distance(a2, a3)

        if d1 == (d2 + d3):
            return False
    return True


def find_station(map_data):
    grid = [[x for x in line] for line in map_data.splitlines()]
    rows, cols = len(grid), len(grid[0])
    asteroids = set()
    for x in range(cols):
        for y in range(rows):
            if grid[y][x] is '#':
                asteroids.add((x, y))
                print(x,y)
    dict = {}
    for station in asteroids:
        if station != (1, 0):
            continue
        count = 0
        for asteroid1 in asteroids:
            if station == asteroid1:
                continue
            if los(asteroids, station, asteroid1):
                print(station, asteroid1)
                count +=1

        dict[station] = count
    # print('\n'.join(' '.join(x for x in row) for row in grid))

    for k, v in dict.items():
        grid[k[1]][k[0]] = v

    # print(dict)
    print('\n'.join(' '.join(str(x) for x in row) for row in grid))
    return


with open('input', 'r') as f:
    asteroid_map = f.read()

find_station(asteroid_map)