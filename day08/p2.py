import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip()

    numbers = [int(x) for x in data.split()]

    def node_value(i):
        child_qty = numbers[i]
        meta_qty = numbers[i + 1]
        i += 2
        child_values = []

        for _ in range(child_qty):
            child_value, i = node_value(i)
            child_values.append(child_value)

        meta_values = numbers[i:i + meta_qty]
        i += meta_qty

        if child_qty == 0:
            return sum(meta_values), i
        else:
            total = 0
            for meta in meta_values:
                if 1 <= meta <= child_qty:
                    total += child_values[meta - 1]
            return total, i

    print(node_value(0)[0])

if __name__ == '__main__':
    main()
