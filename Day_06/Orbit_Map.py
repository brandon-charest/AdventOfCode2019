def find_orbits(orbit_data):
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

    return sum([count_orbits(k) for k in orbit_graph.keys()])


with open('input', 'r') as f:
    data = f.read()
print(find_orbits(data))
