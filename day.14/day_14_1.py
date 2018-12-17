import sys

def do_test_case(total_recipes):
    recipes = [3, 7]
    elf_first = 0
    elf_second = 1

    while len(recipes) < total_recipes + 10:
        new_recipe_whole = recipes[elf_first] + recipes[elf_second]
        if new_recipe_whole >= 10:
            a = new_recipe_whole // 10
            recipes.append(a)

        b = new_recipe_whole % 10
        recipes.append(b)

        elf_first = (elf_first + recipes[elf_first] + 1) % len(recipes)
        elf_second = (elf_second + recipes[elf_second] + 1) % len(recipes)

    print(''.join([str(x) for x in recipes[total_recipes:(total_recipes + 10)]]))


def main():
    for line in sys.stdin:
        do_test_case(int(line))


if __name__ == '__main__':
    main()
