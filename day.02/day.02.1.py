import sys
from collections import Counter

double = 0
triple = 0

for line in sys.stdin:
    count = Counter(list(line))
    if 2 in count.values():
        double += 1
    if 3 in count.values():
        triple += 1

print(str(double * triple))
