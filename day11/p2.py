import sys

GRID_SIZE = 300


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

    prefix_sums = [[0] * (GRID_SIZE + 1) for _ in range(GRID_SIZE + 1)]

    for y in range(1, GRID_SIZE + 1):
        for x in range(1, GRID_SIZE + 1):
            prefix_sums[y][x] = (
                cells[y - 1][x - 1]
                + prefix_sums[y - 1][x]
                + prefix_sums[y][x - 1]
                - prefix_sums[y - 1][x - 1]
            )

    max_power = float("-inf")
    max_square = (0, 0, 0)

    for size in range(1, GRID_SIZE + 1):
        for y in range(1, GRID_SIZE - size + 2):
            for x in range(1, GRID_SIZE - size + 2):
                total_power = (
                    prefix_sums[y + size - 1][x + size - 1]
                    - prefix_sums[y - 1][x + size - 1]
                    - prefix_sums[y + size - 1][x - 1]
                    + prefix_sums[y - 1][x - 1]
                )
                if total_power > max_power:
                    max_power = total_power
                    max_square = (x, y, size)

    print(*max_square, sep=",")


if __name__ == "__main__":
    main()
