import sys
from collections import defaultdict

GENERATIONS = 20


def main():
    with open(sys.argv[1]) as f:
        initial_state, rules_data = f.read().strip().split('\n\n')

    initial_state = initial_state.split(': ')[1]
    rules = dict(line.split(' => ') for line in rules_data.splitlines())

    state = defaultdict(lambda: '.', enumerate(initial_state))
    start_index = -2

    for _ in range(GENERATIONS):
        next_state = defaultdict(lambda: '.')
        for index in range(start_index, len(state) + 2):
            pattern = ''.join(state[i] for i in range(index - 2, index + 3))
            next_state[index] = rules.get(pattern, '.')
        state = next_state
        if state[start_index] == '#':
            start_index -= 2
        elif state[start_index + 1] == '#':
            start_index -= 1

    print(sum(index for index, pot in state.items() if pot == '#'))


if __name__ == '__main__':
    main()
