import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    claims = []
    for line in data:
        coords, size = line.split(' @ ')[1].split(': ')
        x1, y1 = map(int, coords.split(','))
        w, h = map(int, size.split('x'))
        x2, y2 = x1 + w - 1, y1 + h - 1
        claims.append((x1, y1, x2, y2))

    for i, (x1a, y1a, x2a, y2a) in enumerate(claims):
        overlap = False
        for j, (x1b, y1b, x2b, y2b) in enumerate(claims):
            if i == j:
                continue
            if not (x2a < x1b or x1a > x2b or y2a < y1b or y1a > y2b):
                overlap = True
                break

        if not overlap:
            print(i + 1)
            break

if __name__ == '__main__':
    main()
