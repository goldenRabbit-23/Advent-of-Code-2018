import sys
from collections import deque


ADJACENT_OFFSETS = ((-1, 0), (0, -1), (0, 1), (1, 0))


class Unit:
    def __init__(self, unit_type, r, c):
        self.type = unit_type
        self.r = r
        self.c = c
        self.hp = 200
        self.atk = 3
        self.is_alive = True

    @property
    def position(self):
        return self.r, self.c

    def __lt__(self, other):
        return self.position < other.position


class Game:
    def __init__(self, game_map):
        self.walls = set()
        self.units = []
        self.load_map(game_map)

    def load_map(self, game_map):
        for r, row in enumerate(game_map):
            for c, cell in enumerate(row):
                if cell == '#':
                    self.walls.add((r, c))
                elif cell in ('E', 'G'):
                    self.units.append(Unit(cell, r, c))

    @staticmethod
    def adjacent_positions(position):
        r, c = position
        return [(r + dr, c + dc) for dr, dc in ADJACENT_OFFSETS]

    def occupied_positions(self):
        return {unit.position for unit in self.units if unit.is_alive}

    def distances_from(self, start, blocked):
        distances = {start: 0}
        queue = deque([start])

        while queue:
            position = queue.popleft()

            for adjacent in self.adjacent_positions(position):
                if (
                    adjacent not in distances
                    and adjacent not in self.walls
                    and adjacent not in blocked
                ):
                    distances[adjacent] = distances[position] + 1
                    queue.append(adjacent)

        return distances

    def run(self):
        self.units.sort()

        for unit in self.units:
            if not unit.is_alive:
                continue

            enemies = [
                other
                for other in self.units
                if other.is_alive and other.type != unit.type
            ]
            if not enemies:
                return False

            self.move(unit, enemies)
            self.attack(unit, enemies)

        self.units = [unit for unit in self.units if unit.is_alive]
        return True

    def move(self, unit, enemies):
        adjacent = self.adjacent_positions(unit.position)
        if any(enemy.position in adjacent for enemy in enemies):
            return

        occupied = self.occupied_positions()
        in_range = {
            position
            for enemy in enemies
            for position in self.adjacent_positions(enemy.position)
            if position not in self.walls and position not in occupied
        }

        blocked = occupied - {unit.position}
        distances = self.distances_from(unit.position, blocked)
        reachable = [position for position in in_range if position in distances]
        if not reachable:
            return

        destination = min(reachable, key=lambda position: (distances[position], position))
        distances_to_destination = self.distances_from(destination, blocked)

        possible_steps = [
            position
            for position in adjacent
            if position in distances_to_destination and position not in blocked
        ]
        unit.r, unit.c = min(
            possible_steps,
            key=lambda position: (distances_to_destination[position], position),
        )

    def attack(self, unit, enemies):
        adjacent = self.adjacent_positions(unit.position)
        targets = [enemy for enemy in enemies if enemy.position in adjacent]
        if not targets:
            return

        target = min(targets, key=lambda enemy: (enemy.hp, enemy.position))
        target.hp -= unit.atk
        if target.hp <= 0:
            target.is_alive = False


def main():
    with open(sys.argv[1]) as f:
        game_map = f.read().strip().splitlines()

    game = Game(game_map)
    rounds = 0

    while game.run():
        rounds += 1

    remaining_hp = sum(unit.hp for unit in game.units if unit.is_alive)
    print(rounds * remaining_hp)


if __name__ == '__main__':
    main()
