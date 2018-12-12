import sys

num = []
spotted = []

for line in sys.stdin:
    num.append(int(line))

totalNum = len(num)
currentFreq = 0
index = 0

while currentFreq not in spotted:
    spotted.append(currentFreq)
    currentFreq += num[index]
    index = (index + 1) % totalNum

print(currentFreq)
