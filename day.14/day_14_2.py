import sys

def do_test_case(to_match):
    recipes = [3, 7]
    elf_first = 0
    elf_second = 1

    while True:
        if (len(recipes) >= len(to_match)):
            last_string = recipes[(len(recipes) - len(to_match) - 1): (len(recipes) - 1)]
            if last_string == to_match:
                print(str(len(recipes) - len(to_match) - 1))
                break
            last_string = recipes[(len(recipes) - len(to_match)): (len(recipes))]
            if last_string == to_match:
                print(str(len(recipes) - len(to_match)))
                break

        new_recipe_whole = recipes[elf_first] + recipes[elf_second]
        if new_recipe_whole >= 10:
            a = new_recipe_whole // 10
            recipes.append(a)

        b = new_recipe_whole % 10
        recipes.append(b)

        elf_first = (elf_first + recipes[elf_first] + 1) % len(recipes)
        elf_second = (elf_second + recipes[elf_second] + 1) % len(recipes)


def main():
    for line in sys.stdin:
        do_test_case([int(x) for x in list(line.replace('\n', ''))])


if __name__ == '__main__':
    main()
