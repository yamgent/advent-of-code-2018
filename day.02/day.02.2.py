from collections import Counter
import sys

def discard(string, stringlen, pos):
    return string[0:pos] + string[(pos + 1):]

def main():
    boxes = sys.stdin.readlines()
    strlen = len(boxes[0])

    for i in range(0, strlen):
        remove_char = [discard(x, strlen, i) for x in boxes]
        count = Counter(remove_char)
        for k, v in count.items():
            if v == 2:
                print(k[:-1])  # remove '\n'
                return

main()
