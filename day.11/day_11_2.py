# TODO: Any way to optimize this? Runs slow on Python


def group(cells, cell_size, group_size):
    temp = []
    shorten_size = (cell_size - group_size + 1)

    for y in range(0, cell_size):
        cur_row = [0] * shorten_size
        for x in range(0, shorten_size):
            cur_row[x] = sum(cells[y][x:x+group_size])
        temp.append(cur_row)

    result = []
    for y in range(0, shorten_size):
        cur_row = [0] * shorten_size
        for x in range(0, shorten_size):
            for i in range(y, y + group_size):
                cur_row[x] += temp[i][x]
        result.append(cur_row)

    return result


def generate_cells(serial, size):
    cells = []
    for y in range(0, size):
        cur_row = [0] * size

        for x in range(0, size):
            rack_id = x + 10
            cur_row[x] = (((rack_id * (y * rack_id + serial)) // 100) % 10) - 5

        cells.append(cur_row)

    return cells


def find_max(values):
    max_so_far = values[0][0]
    max_x = 0
    max_y = 0

    for y in range(0, len(values)):
        for x in range(0, len(values[y])):
            if max_so_far < values[y][x]:
                max_x = x
                max_y = y
                max_so_far = values[y][x]
    
    return max_x, max_y


def print_region(original, top, left, size):
    for y in range(top, top + size):
        print(original[y][left:(left+size)])


def main():
    serial = int(input())
    cell_size = 301
    original = generate_cells(serial, cell_size)

    group_power = [0] * cell_size
    group_max_x = [0] * cell_size
    group_max_y = [0] * cell_size

    for group_size in range(3, 300):
        grouped = group(original, cell_size, group_size)

        max_x, max_y = find_max(grouped)
        power = grouped[max_y][max_x]

        print(str(max_x) + ',' + str(max_y) + ',' + str(group_size))
        # print('power: ' + str(power))
        # print_region(original, max_y, max_x, 3)

        group_max_x[group_size] = max_x
        group_max_y[group_size] = max_y
        group_power[group_size] = power

    max_power = max(group_power)
    max_power_size = group_power.index(max_power)
    print(str(group_max_x[max_power_size]) + ',' + str(group_max_y[max_power_size]) + ',' + str(max_power_size))

main()
