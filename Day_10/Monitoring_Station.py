import math

def get_angle(p1, p2):
    result = math.atan2(p2[0] - p1[0], p1[1] - p2[1]) * 180 / math.pi
    if result < 0:
        return 360 + result
    return result

def find_station(map_data):
    grid = [[x for x in line] for line in map_data.splitlines()]
    rows, cols = len(grid), len(grid[0])
    asteroids = set()
    for x in range(cols):
        for y in range(rows):
            if grid[y][x] is '#':
                asteroids.add((x, y))


    max_count = 0
    result = None
    for station in asteroids:
        count = set()
        for asteroid in asteroids:
            if station == asteroid:
                continue
            count.add(get_angle(station, asteroid))
            if len(count) > max_count:
                max_count = len(count)
                result = station
        # just for visualization
        #grid[station[1]][station[0]] = len(count)



    print(result, max_count)
    print('\n'.join(' '.join(str(x) for x in row) for row in grid))
    return


with open('input', 'r') as f:
    asteroid_map = f.read()

find_station(asteroid_map)