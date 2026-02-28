import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    players, marbles = int((p := data.split())[0]), int(p[6])
    scores = [0] * players
    circle = [0]
    pos = 0

    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            pos = (pos - 7) % len(circle)
            scores[marble % players] += marble + circle.pop(pos)
        else:
            pos = (pos + 2) % len(circle)
            circle.insert(pos, marble)

    print(max(scores))

if __name__ == '__main__':
    main()
