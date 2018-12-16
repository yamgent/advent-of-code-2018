def group(cells):
    temp = []
    for y in range(0, 300):
        cur_row = [0] * 298
        for x in range(0, 298):
            cur_row[x] = sum(cells[y][x:x+3])
        temp.append(cur_row)

    result = []
    for y in range(0, 298):
        cur_row = [0] * 298
        for x in range(0, 298):
            cur_row[x] = temp[y][x] + temp[y+1][x] + temp[y+2][x]
        result.append(cur_row)

    return result


def generate_cells(serial):
    cells = []
    for y in range(0, 300):
        cur_row = [0] * 300

        for x in range(0, 300):
            rack_id = x + 10
            cur_row[x] = (((rack_id * (y * rack_id + serial)) // 100) % 10) - 5

        cells.append(cur_row)

    return cells


def find_max(values):
    max_so_far = values[0][0]
    max_x = 0
    max_y = 0

    for y in range(0, 298):
        for x in range(0, 298):
            if max_so_far < values[y][x]:
                max_x = x
                max_y = y
                max_so_far = values[y][x]
    
    return max_x, max_y


def print_region(original, top, left):
    for y in range(top, top + 3):
        print(original[y][left:(left+3)])


def main():
    serial = int(input())
    original = generate_cells(serial)
    grouped = group(original)
    max_x, max_y = find_max(grouped)

    print(str(max_x) + ',' + str(max_y))

    # print('power: ' + str(grouped[max_y][max_x]))
    # print_region(original, max_y, max_x)


main()
