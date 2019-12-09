def find_orbits(orbit_data, find_path=False):
    orbits = [x for x in orbit_data.split('\n')]
    orbit_graph = {}

    def count_orbits(data):
        if data not in orbit_graph:
            return 0
        else:
            return len(orbit_graph[data]) + sum([count_orbits(x) for x in orbit_graph[data]])

    for planets in orbits:
        planet1, planet2 = planets.split(')')
        if planet1 in orbit_graph.keys():
            orbit_graph[planet1].append(planet2)
        else:
            orbit_graph[planet1] = [planet2]

    def dfs_paths(graph, start, goal):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                if vertex in graph:
                    for neighbor in graph[vertex]:
                        stack.append((neighbor, path + [neighbor]))

    # this is pretty ugly :( but it works
    if find_path:
        you = dfs_paths(orbit_graph, 'COM', 'YOU')
        san = dfs_paths(orbit_graph, 'COM', 'SAN')
        both = [x for x in you if x in san]
        return (len(you) - len(both) + len(san) - len(both)) - 2
    else:
        return sum([count_orbits(k) for k in orbit_graph.keys()])


with open('input', 'r') as f:
    data = f.read()
print(find_orbits(data, find_path=True))
