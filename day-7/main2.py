
import pprint
from collections import deque
pp = pprint.PrettyPrinter(indent=4)

f = open("input.txt", "r")


def getCurrentLineNums(line, separator=','):
    filtered = list(
        filter(lambda x: x != '', line.rstrip("\n").split(separator)))

    return list(map(lambda x: int(x), filtered))


values = [0] * 2000

for i in getCurrentLineNums(f.readline()):
    values[i] += 1


def getDiff(i, j):
    n = abs(i - j)
    return int(n * (n+1) / 2)


answer = float("inf")
for i in range(len(values)):

    result = 0

    for j in range(len(values)):
        result += getDiff(i, j) * values[j]

    print(result)

    answer = min(answer, result)
# print(values)
print(answer)

# print(getDiff(3))
