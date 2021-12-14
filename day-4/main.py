
import pprint
from collections import defaultdict
pp = pprint.PrettyPrinter(indent=4)

f = open("input.txt", "r")


def getCurrentLineNums(line, separator=' '):

    return filter(lambda x: x != '', line.rstrip("\n").split(separator))


nums = getCurrentLineNums(f.readline(), ',')

grids = []
gridsContainingNum = defaultdict(list)

while True:
    previousLine = f.readline()
    if previousLine == '':
        break

    current = {"columns": [0] * 5, "rows": [0] * 5, "nums": {}}

    for rowIndex in range(5):
        row = getCurrentLineNums(f.readline())

        for columnIndex, num in enumerate(row):
            current["nums"][num] = [rowIndex, columnIndex, False]

            gridsContainingNum[num].append((len(grids), current))

    grids.append(current)


def getAnswer():

    winners = set()
    firstResult = 0
    lastResult = 0
    for num in nums:
        for gridIndex, grid in gridsContainingNum[num]:

            if gridIndex in winners:
                continue

            if num not in grid["nums"]:
                continue

            row, column, _ = grid["nums"][num]

            # The first position saves row, the second col and the third one seen
            grid["nums"][num][2] = True

            grid["rows"][row] += 1
            grid["columns"][column] += 1

            if grid["rows"][row] != 5 and grid["columns"][column] != 5:
                continue

            current = 0
            for notSeenNum in grid["nums"]:
                if grid["nums"][notSeenNum][2] == False:
                    current += int(notSeenNum)

            if len(winners) == 0:
                firstResult = current * int(num)

            lastResult = current * int(num)

            winners.add(gridIndex)

    return firstResult, lastResult


print(getAnswer())
# pp.pprint(grids)
