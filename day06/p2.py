import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    coords = [tuple(map(int, line.split(', '))) for line in data]
    xs, ys = zip(*coords)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    count = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            count += sum(abs(x - cx) + abs(y - cy) for cx, cy in coords) < 10000

    print(count)

if __name__ == '__main__':
    main()
