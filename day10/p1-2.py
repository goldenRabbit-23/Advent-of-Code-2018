import re
import sys

NUMBER_PATTERN = re.compile(r'-?\d+')


def parse_points(lines):
    positions = []
    velocities = []

    for line in lines:
        x, y, vx, vy = map(int, NUMBER_PATTERN.findall(line))
        positions.append((x, y))
        velocities.append((vx, vy))

    return positions, velocities


def bounds(positions):
    xs, ys = zip(*positions)
    return min(xs), max(xs), min(ys), max(ys)


def bounding_box_area(positions):
    min_x, max_x, min_y, max_y = bounds(positions)
    return (max_x - min_x) * (max_y - min_y)


def find_message(positions, velocities):
    seconds = 0
    area = bounding_box_area(positions)

    while True:
        next_positions = [
            (x + vx, y + vy)
            for (x, y), (vx, vy) in zip(positions, velocities)
        ]
        next_area = bounding_box_area(next_positions)

        if next_area > area:
            return positions, seconds

        positions = next_positions
        area = next_area
        seconds += 1


def print_positions(positions):
    min_x, max_x, min_y, max_y = bounds(positions)
    occupied = set(positions)

    for y in range(min_y, max_y + 1):
        print(''.join(
            '#' if (x, y) in occupied else ' '
            for x in range(min_x, max_x + 1)
        ))


def main():
    with open(sys.argv[1]) as f:
        positions, velocities = parse_points(f)

    positions, seconds = find_message(positions, velocities)
    print(f'After {seconds} seconds:')
    print_positions(positions)

if __name__ == '__main__':
    main()
