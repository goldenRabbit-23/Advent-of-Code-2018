import sys

OPERATIONS = [
    'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
    'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'
]


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


def find_valid_operations(a, b, c, registers, after):
    matching_operations = set()

    for opcode in range(16):
        new_registers = registers.copy()
        operation(opcode, a, b, c, new_registers)
        if new_registers == after:
            matching_operations.add(OPERATIONS[opcode])

    return matching_operations


def main():
    with open(sys.argv[1]) as f:
        samples, program = f.read().strip().split('\n\n\n\n')

    candidates = {op: set(OPERATIONS) for op in range(16)}

    for sample in samples.split('\n\n'):
        before, instruction, after = sample.split('\n')
        before = list(map(int, before.split(': ')[1][1:-1].split(', ')))
        opcode, a, b, c = map(int, instruction.split())
        after = list(map(int, after.split(':  ')[1][1:-1].split(', ')))

        valid_ops = find_valid_operations(a, b, c, before, after)
        candidates[opcode] &= valid_ops

    # Deduce the mapping of opcodes to operations
    opcode_mapping = {}

    while len(opcode_mapping) < 16:
        for opcode, ops in candidates.items():
            if opcode not in opcode_mapping and len(ops) == 1:
                op = next(iter(ops))
                opcode_mapping[opcode] = op
                for other_opcode, other_ops in candidates.items():
                    if other_opcode != opcode:
                        other_ops.discard(op)

    registers = [0, 0, 0, 0]

    for instruction in program.splitlines():
        opcode, a, b, c = map(int, instruction.split())
        op_name = opcode_mapping[opcode]
        op_index = OPERATIONS.index(op_name)
        operation(op_index, a, b, c, registers)

    print(registers[0])


if __name__ == '__main__':
    main()
