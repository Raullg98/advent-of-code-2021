
import pprint
from collections import defaultdict
pp = pprint.PrettyPrinter(indent=4)


def getCurrentLineNums(line):
    return [[int(x) for x in val.split(',')] for val in line.rstrip("\n").split(' -> ')]


def getAnswer(isChallengeTwo):
    count = defaultdict(int)
    f = open("input.txt", "r")
    for line in f:
        fromValues, toValues = getCurrentLineNums(line)

        if fromValues[0] == toValues[0]:

            for i in range(min(fromValues[1], toValues[1]), max(fromValues[1], toValues[1]) + 1):
                count[(fromValues[0], i)] += 1
        elif fromValues[1] == toValues[1]:
            for i in range(min(fromValues[0], toValues[0]), max(fromValues[0], toValues[0]) + 1):
                count[(i, fromValues[1])] += 1
        elif isChallengeTwo:

            while fromValues[0] != toValues[0] and fromValues[1] != toValues[1]:

                count[(fromValues[0], fromValues[1])] += 1
                fromValues[0] += 1 if fromValues[0] < toValues[0] else -1
                fromValues[1] += 1 if fromValues[1] < toValues[1] else -1

            count[(toValues[0], toValues[1])] += 1
    result = 0

    for i in count.values():
        if i >= 2:
            result += 1

    return result


print(getAnswer(False), getAnswer(True))
