import sys

GENERATIONS = 50000000000


def main():
    with open(sys.argv[1]) as f:
        initial_state, rules_data = f.read().strip().split('\n\n')

    initial_state = initial_state.split(': ')[1]
    rules = dict(line.split(' => ') for line in rules_data.splitlines())

    state = {
        index
        for index, pot in enumerate(initial_state)
        if pot == '#'
    }

    seen = {}
    generation = 0

    while generation < GENERATIONS:
        leftmost = min(state)
        normalized_state = tuple(index - leftmost for index in sorted(state))

        if normalized_state in seen:
            prev_generation, prev_leftmost = seen[normalized_state]

            cycle_length = generation - prev_generation
            cycle_shift = leftmost - prev_leftmost
            remaining = GENERATIONS - generation
            cycles_to_skip = remaining // cycle_length

            if cycles_to_skip:
                total_shift = cycles_to_skip * cycle_shift
                state = {index + total_shift for index in state}
                generation += cycles_to_skip * cycle_length
                continue
        else:
            seen[normalized_state] = (generation, leftmost)

        next_state = set()

        for index in range(min(state) - 2, max(state) + 3):
            pattern = ''.join(
                '#' if neighbor in state else '.'
                for neighbor in range(index - 2, index + 3)
            )
            if rules.get(pattern, '.') == '#':
                next_state.add(index)

        state = next_state
        generation += 1

    print(sum(state))


if __name__ == '__main__':
    main()
