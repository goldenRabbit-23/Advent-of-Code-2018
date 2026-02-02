import sys
from itertools import cycle

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    seen = {0}
    freq = 0

    for x in cycle(data):
        freq += int(x)
        if freq in seen:
            print(freq)
            return
        seen.add(freq)

if __name__ == '__main__':
    main()
