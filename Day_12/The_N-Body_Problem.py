import re


class Position:
    def __init__(self, data):
        vals = re.findall("-?\\d+", data)
        self.x = int(vals[0])
        self.y = int(vals[1])
        self.z = int(vals[2])

    def update_pos(self, data):
        x, y, z = data
        self.x += x
        self.y += y
        self.z += z

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_pos(self):
        return [self.x, self.y, self.z]

    def get_pos_string(self):
        return f"pos=<x={self.x}, y={self.y}, z={self.z}>"


class Velocity:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def update_vel(self, vel_data):
        x,y,z = vel_data
        self.x += int(x)
        self.y += int(y)
        self.z += int(z)

    def kinetic_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_vel(self):
        return[self.x, self.y, self.z]

    def get_vel_string(self):
        return f"vel=<x={self.x}, y={self.y}, z={self.z}>"


class Moon:
    def __init__(self, data):
        self._pos = Position(data)
        self._vel = Velocity()

    def update_vel(self, data):
        self._vel.update_vel(data)

    def update_pos(self):
        self._pos.update_pos(self._vel.get_vel())

    def get_vel(self):
        return self._vel.get_vel()

    def get_pos(self):
        return self._pos.get_pos()

    def get_energy(self):
        return self._pos.potential_energy() * self._vel.kinetic_energy()

    def info(self):
        return f"{self._pos.get_pos_string():<25}||{self._vel.get_vel_string():>22}"


def update_moons(moons):
    for m1 in moons:
        m1_x, m1_y, m1_z = m1.get_pos()
        grav_x, grav_y, grav_z = 0, 0, 0
        for m2 in moons:
            if m1 == m2:
                continue
            m2_x, m2_y, m2_z = m2.get_pos()
            grav_x += 1 if m1_x < m2_x else -1 if m1_x > m2_x else 0
            grav_y += 1 if m1_y < m2_y else -1 if m1_y > m2_y else 0
            grav_z += 1 if m1_z < m2_z else -1 if m1_z > m2_z else 0
        m1.update_vel([grav_x, grav_y, grav_z])
    for moon in moons:
        moon.update_pos()
    return


def part_one(moons):
    steps = 0
    for i in range(1000):
        print(f'After {steps} steps:')
        for m in moons:
            print(m.info())
        update_moons(moons)
        steps += 1

    total = 0
    for j in moons:
        total += j.get_energy()
    print(total)
    return

moons = []
with open('input', 'r') as f:
    for line in f:
        moons.append(Moon(line))
