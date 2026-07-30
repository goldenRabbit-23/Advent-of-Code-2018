import sys


def main():
    with open(sys.argv[1]) as f:
        goal = [int(digit) for digit in f.read().strip()]

    goal_len = len(goal)
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        total = recipes[elf1] + recipes[elf2]
        if total >= 10:
            recipes.append(total // 10)
            if recipes[-goal_len:] == goal:
                print(len(recipes) - goal_len)
                return

        recipes.append(total % 10)
        if recipes[-goal_len:] == goal:
            print(len(recipes) - goal_len)
            return

        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)


if __name__ == '__main__':
    main()
