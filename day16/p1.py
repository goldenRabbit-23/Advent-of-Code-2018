import sys


def operation(opcode, a, b, c, registers):
    if opcode == 0:
        registers[c] = registers[a] + registers[b]
    elif opcode == 1:
        registers[c] = registers[a] + b
    elif opcode == 2:
        registers[c] = registers[a] * registers[b]
    elif opcode == 3:
        registers[c] = registers[a] * b
    elif opcode == 4:
        registers[c] = registers[a] & registers[b]
    elif opcode == 5:
        registers[c] = registers[a] & b
    elif opcode == 6:
        registers[c] = registers[a] | registers[b]
    elif opcode == 7:
        registers[c] = registers[a] | b
    elif opcode == 8:
        registers[c] = registers[a]
    elif opcode == 9:
        registers[c] = a
    elif opcode == 10:
        registers[c] = int(a > registers[b])
    elif opcode == 11:
        registers[c] = int(registers[a] > b)
    elif opcode == 12:
        registers[c] = int(registers[a] > registers[b])
    elif opcode == 13:
        registers[c] = int(a == registers[b])
    elif opcode == 14:
        registers[c] = int(registers[a] == b)
    elif opcode == 15:
        registers[c] = int(registers[a] == registers[b])


def try_all_operations(a, b, c, registers, after):
    matches = 0

    for opcode in range(16):
        new_registers = registers.copy()
        operation(opcode, a, b, c, new_registers)
        if new_registers == after:
            matches += 1

    return matches >= 3


def main():
    with open(sys.argv[1]) as f:
        samples = f.read().strip().split('\n\n\n\n')[0]

    count = 0

    for sample in samples.split('\n\n'):
        before, instruction, after = sample.split('\n')
        before = list(map(int, before.split(': ')[1][1:-1].split(', ')))
        _, a, b, c = map(int, instruction.split())
        after = list(map(int, after.split(':  ')[1][1:-1].split(', ')))

        if try_all_operations(a, b, c, before, after):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
