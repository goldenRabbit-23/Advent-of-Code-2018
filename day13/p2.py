import sys

# Direction indices: up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    with open(sys.argv[1]) as f:
        track = f.read().splitlines()

    carts = []
    for r, row in enumerate(track):
        for c, tr in enumerate(row):
            if tr in '<>^v':
                carts.append((r, c, '^>v<'.index(tr), 0))

    # Intersection turns cycle through left, straight, and right.
    while len(carts) > 1:
        carts.sort()
        occupied = {(r, c) for r, c, _, _ in carts}
        next_carts = []

        for cr, cc, cd, ci in carts:
            # Skip carts removed by a collision before their turn.
            if (cr, cc) not in occupied:
                continue

            occupied.remove((cr, cc))

            dr, dc = DIRECTIONS[cd]
            nr, nc = cr + dr, cc + dc

            if (nr, nc) in occupied:
                occupied.remove((nr, nc))
                next_carts = [
                    cart for cart in next_carts
                    if (cart[0], cart[1]) != (nr, nc)
                ]
                continue

            tr = track[nr][nc]
            nd, ni = cd, ci

            if tr == '+':
                if ci == 0:
                    nd = (cd - 1) % 4
                elif ci == 2:
                    nd = (cd + 1) % 4
                ni = (ci + 1) % 3
            elif tr == '/':
                nd = (cd + 1) % 4 if cd in (0, 2) else (cd - 1) % 4
            elif tr == '\\':
                nd = (cd - 1) % 4 if cd in (0, 2) else (cd + 1) % 4

            occupied.add((nr, nc))
            next_carts.append((nr, nc, nd, ni))

        carts = next_carts

    cr, cc, _, _ = carts[0]
    print(f'{cc},{cr}')


if __name__ == '__main__':
    main()
