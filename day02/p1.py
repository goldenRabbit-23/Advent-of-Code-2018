import sys
from collections import Counter

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    two, three = 0, 0

    for line in data:
        counts = set(Counter(line).values())
        if 2 in counts:
            two += 1
        if 3 in counts:
            three += 1

    print(two * three)

if __name__ == '__main__':
    main()
