import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    print(sum(int(x) for x in data))

if __name__ == '__main__':
    main()
