import sys

num = [int(line) for line in sys.stdin.readlines()]
spotted = {}

totalNum = len(num)
currentFreq = 0
index = 0

while currentFreq not in spotted:
    spotted[currentFreq] = True
    currentFreq += num[index]
    index = (index + 1) % totalNum

print(currentFreq)
