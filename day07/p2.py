import sys
from collections import defaultdict
from heapq import heappop, heappush

def step_duration(step):
    return 60 + ord(step) - ord('A') + 1

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

    workers = []  # (finish_time, step)
    time = 0

    while heap or workers:
        # Assign work to free workers
        while heap and len(workers) < 5:
            step = heappop(heap)
            heappush(workers, (time + step_duration(step), step))

        # Advance to next completion
        time, done = heappop(workers)
        for nxt in nexts[done]:
            deps[nxt].discard(done)
            if not deps[nxt]:
                heappush(heap, nxt)

    print(time)

if __name__ == '__main__':
    main()
