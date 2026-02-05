import sys

def react(polymer):
    stack = []

    for c in polymer:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)

    return len(stack)

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    units = set(data.lower())
    best = float('inf')

    for unit in units:
        modified = [c for c in data if c.lower() != unit]
        length = react(modified)
        best = min(best, length)

    print(best)

if __name__ == '__main__':
    main()
