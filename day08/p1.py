import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    numbers = [int(x) for x in data.split()]

    def sum_metadata(i):
        child_qty = numbers[i]
        meta_qty = numbers[i + 1]
        i += 2
        total = 0

        for _ in range(child_qty):
            child_total, i = sum_metadata(i)
            total += child_total

        total += sum(numbers[i:i + meta_qty])
        i += meta_qty

        return total, i

    print(sum_metadata(0)[0])

if __name__ == '__main__':
    main()
