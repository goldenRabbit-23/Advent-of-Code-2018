import sys
from itertools import combinations

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    for a, b in combinations(data, 2):
        diffs = [x for x, y in zip(a, b) if x != y]
        if len(diffs) == 1:
            print(''.join(x for x, y in zip(a, b) if x == y))
            break

if __name__ == '__main__':
    main()
