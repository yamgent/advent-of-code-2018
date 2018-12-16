import sys

def main():
    input_state = list(input().replace('initial state: ', ''))
    input()

    # 20 generation total, so each generation might be lengthen by 4 on both sides -> at least 80 more spots needed
    extra_empty_spot = 20 * 5
    state_old = ['.'] * (len(input_state) + extra_empty_spot)
    zero_position = extra_empty_spot // 2
    for i in range(0, len(input_state)):
        state_old[zero_position + i] = input_state[i]

    change = {}

    for line in sys.stdin:
        line_read = line.replace(' => ', '')
        change[line_read[0:5]] = line_read[5]

    for g in range(0, 20):
        state_new = ['.'] * len(state_old)
        for i in range(2, len(state_old) - 5):
            neighbours = ''.join(state_old[i-2:(i+3)])
            if neighbours in change:
                state_new[i] = change[neighbours]
            else:
                state_new[i] = '.'

        state_old = state_new

        # print(''.join(state_old))

    result = 0
    for i in range(0, len(state_old)):
        if state_old[i] == '#':
            result += (i - zero_position)
    print(result)

main()