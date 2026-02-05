import sys
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    coords = [tuple(map(int, line.split(', '))) for line in data]
    xs, ys = zip(*coords)
    min_x, max_x = min(xs) - 1, max(xs) + 1
    min_y, max_y = min(ys) - 1, max(ys) + 1

    area_counts = defaultdict(int)
    infinite = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            best = second = float('inf')
            best_coord = None

            for cx, cy in coords:
                d = abs(x - cx) + abs(y - cy)
                if d < best:
                    best, second = d, best
                    best_coord = (cx, cy)
                elif d < second:
                    second = d

            if best == second:
                continue

            area_counts[best_coord] += 1

            if x == min_x or x == max_x or y == min_y or y == max_y:
                infinite.add(best_coord)

    print(max(area_counts[c] for c in coords if c not in infinite))

if __name__ == '__main__':
    main()
