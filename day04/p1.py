import sys
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    timeline = {}
    guard_sleep_per_minute = defaultdict(lambda: [0] * 60)  # guard ID -> [minutes asleep count]
    guard_total_sleep = defaultdict(int)  # guard ID -> total minutes asleep

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
                guard_sleep_per_minute[current_guard][m] += 1
            guard_total_sleep[current_guard] += (minute - sleep_start)

    sleepiest_guard = max(guard_total_sleep, key=guard_total_sleep.get)
    sleepiest_minute_counts = guard_sleep_per_minute[sleepiest_guard]
    sleepiest_minute = sleepiest_minute_counts.index(max(sleepiest_minute_counts))

    print(sleepiest_guard * sleepiest_minute)

if __name__ == '__main__':
    main()
