import re
import sys


LINE_PATTERN = re.compile(r"([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)")


def parse_clay(lines):
    clay = set()

    for line in lines:
        match = LINE_PATTERN.fullmatch(line)
        if match is None:
            raise ValueError(f"Invalid scan line: {line!r}")

        fixed_axis, fixed, _, start, end = match.groups()
        fixed, start, end = map(int, (fixed, start, end))

        if fixed_axis == "x":
            clay.update((fixed, y) for y in range(start, end + 1))
        else:
            clay.update((x, fixed) for x in range(start, end + 1))

    return clay


def count_reachable_water(clay):
    min_y = min(y for _, y in clay)
    max_y = max(y for _, y in clay)
    flowing = set()
    settled = set()

    # A vertical path can be deeper than Python's default recursion limit.
    sys.setrecursionlimit(max(2_000, max_y * 2))

    def flow(x, y):
        position = (x, y)

        if y > max_y:
            return False
        if position in clay or position in settled:
            return True
        if position in flowing:
            return False

        flowing.add(position)

        if not flow(x, y + 1):
            return False

        left, left_blocked = spread(x, y, -1)
        right, right_blocked = spread(x, y, 1)

        if not (left_blocked and right_blocked):
            return False

        for current_x in range(left, right + 1):
            position = (current_x, y)
            flowing.discard(position)
            settled.add(position)

        return True

    def spread(x, y, direction):
        """Return the last wet x-coordinate and whether clay blocks this side."""
        current_x = x

        while True:
            next_x = current_x + direction
            if (next_x, y) in clay:
                return current_x, True

            current_x = next_x
            flowing.add((current_x, y))

            if not flow(current_x, y + 1):
                return current_x, False

    flow(500, 0)
    return sum(min_y <= y <= max_y for _, y in settled)


def main():
    with open(sys.argv[1]) as input_file:
        clay = parse_clay(input_file.read().splitlines())

    print(count_reachable_water(clay))


if __name__ == "__main__":
    main()
