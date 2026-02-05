import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    stack = []

    for c in data:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)

    print(len(stack))

if __name__ == '__main__':
    main()
