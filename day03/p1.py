import sys
from collections import Counter

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    c = Counter()
    for line in data:
        coords, size = line.split(' @ ')[1].split(': ')
        x, y = map(int, coords.split(','))
        w, h = map(int, size.split('x'))
        for i in range(x, x + w):
            for j in range(y, y + h):
                c[(i, j)] += 1

    print(sum(1 for v in c.values() if v >= 2))

if __name__ == '__main__':
    main()
