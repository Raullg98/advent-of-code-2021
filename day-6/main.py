
import pprint
from collections import deque
pp = pprint.PrettyPrinter(indent=4)


def getCurrentLineNums(line, separator=','):
    filtered = list(
        filter(lambda x: x != '', line.rstrip("\n").split(separator)))

    return list(map(lambda x: int(x), filtered))


def getAnswer(days):
    queue = deque([0] * 9)
    f = open("input.txt", "r")
    for val in getCurrentLineNums(f.readline()):
        queue[val] += 1

    for day in range(days):

        val = queue.popleft()
        queue[6] += val

        queue.append(val)

    return sum(queue)


print(getAnswer(80), getAnswer(256))
