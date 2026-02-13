import sys
from collections import defaultdict
from heapq import heappop, heappush

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    deps = defaultdict(set)
    nexts = defaultdict(set)
    all_steps = set()

    for line in data:
        parts = line.split()
        prereq, step = parts[1], parts[7]
        deps[step].add(prereq)
        nexts[prereq].add(step)
        all_steps.update([prereq, step])

    heap = []
    for step in all_steps:
        if step not in deps:
            heappush(heap, step)

    result = []

    while heap:
        current = heappop(heap)
        result.append(current)

        for step in nexts[current]:
            deps[step].remove(current)
            if not deps[step]:
                heappush(heap, step)
                del deps[step]

    print(''.join(result))

if __name__ == '__main__':
    main()
