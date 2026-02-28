import sys
from collections import deque

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    players, marbles = int((p := data.split())[0]), int(p[6]) * 100
    scores = [0] * players
    circle = deque([0])

    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(marble)

    print(max(scores))

if __name__ == '__main__':
    main()
