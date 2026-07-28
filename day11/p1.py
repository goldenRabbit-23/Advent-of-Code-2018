import sys

GRID_SIZE = 300
SQUARE_SIZE = 3


def main():
    with open(sys.argv[1]) as f:
        serial = int(f.read().strip())

    cells = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    for y in range(1, GRID_SIZE + 1):
        for x in range(1, GRID_SIZE + 1):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += serial
            power_level *= rack_id
            power_level = (power_level // 100) % 10
            power_level -= 5
            cells[y - 1][x - 1] = power_level

    max_power = float("-inf")
    max_coordinates = (0, 0)

    for y in range(GRID_SIZE - SQUARE_SIZE + 1):
        for x in range(GRID_SIZE - SQUARE_SIZE + 1):
            total_power = sum(
                cells[y + dy][x + dx]
                for dy in range(SQUARE_SIZE)
                for dx in range(SQUARE_SIZE)
            )
            if total_power > max_power:
                max_power = total_power
                max_coordinates = (x + 1, y + 1)

    print(*max_coordinates, sep=",")


if __name__ == "__main__":
    main()
