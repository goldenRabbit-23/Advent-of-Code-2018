import sys
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    timeline = {}
    guard_sleep_per_minute = [defaultdict(int) for _ in range(60)]  # minute -> {guard ID: sleep count}

    for line in data:
        time, action = line.split('] ')
        time = time[1:]
        timeline[time] = action

    sorted_times = sorted(timeline.keys())
    current_guard = None
    sleep_start = 0

    for time in sorted_times:
        action = timeline[time]
        minute = int(time[-2:])

        if 'Guard' in action:
            current_guard = int(action.split()[1][1:])
        elif 'falls asleep' in action:
            sleep_start = minute
        elif 'wakes up' in action:
            for m in range(sleep_start, minute):
                guard_sleep_per_minute[m][current_guard] += 1

    max_sleep = 0
    max_guard = None
    max_minute = None

    for minute, guards in enumerate(guard_sleep_per_minute):
        for guard, sleep_count in guards.items():
            if sleep_count > max_sleep:
                max_sleep = sleep_count
                max_guard = guard
                max_minute = minute

    print(max_guard * max_minute)

if __name__ == '__main__':
    main()
