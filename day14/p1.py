import sys


def main():
    with open(sys.argv[1]) as f:
        goal = int(f.read().strip())

    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipes) < goal + 10:
        total = recipes[elf1] + recipes[elf2]
        if total >= 10:
            recipes.append(total // 10)
        recipes.append(total % 10)

        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    print(''.join(str(score) for score in recipes[goal:goal + 10]))


if __name__ == '__main__':
    main()
