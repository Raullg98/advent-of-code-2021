
import pprint
from collections import deque
pp = pprint.PrettyPrinter(indent=4)

f = open("input.txt", "r")


# Part 1 - O(n)
def getCurrentLineNums(line, separator=','):
    filtered = list(
        filter(lambda x: x != '', line.rstrip("\n").split(separator)))

    return list(map(lambda x: int(x), filtered))


values = [0] * 2000
dp = [0] * 2000

for i in getCurrentLineNums(f.readline()):
    values[i] += 1

accumulator = 0
items = 0
for i in reversed(range(len(values))):
    dp[i] = accumulator
    items += values[i]
    accumulator += items


result = float("inf")
accumulator = 0
items = 0

for i in range(len(values)):
    result = min(result, dp[i] + accumulator)
    items += values[i]
    accumulator += items


print(values)
print(dp)

print(result)
