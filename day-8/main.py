import collections
from typing import Collection


f = open("input.txt", "r")


def sortString(string):
    sorted_characters = sorted(string)
    return "".join(sorted_characters)


def getCurrentLineNums(line, separator=' '):
    firstPart, secondPart = [[list(val) for val in part.split(
        ' ')] for part in line.rstrip("\n").split(' | ')]
    return firstPart, secondPart


def getNum(firstPart, secondPart):
    values = {}
    for num in firstPart:
        numValue = 0
        if len(num) == 2:
            numValue = 1
        elif len(num) == 4:
            numValue = 4
        elif len(num) == 3:
            numValue = 7
        elif len(num) == 7:
            numValue = 8

        values[numValue] = set(num)

    result = 0
    for num in secondPart:
        setNum = set(num)
        numValue = 0
        if len(num) == 2:
            numValue = 1
        elif len(num) == 4:
            numValue = 4
        elif len(num) == 3:
            numValue = 7
        elif len(num) == 7:
            numValue = 8
        elif len(num) == 5 and len(setNum.intersection(values[7])) == len(values[7]):
            numValue = 3
        elif len(num) == 5 and len(setNum.intersection(values[4])) == len(values[4]) - 1:
            numValue = 5
        elif len(num) == 5:
            numValue = 2
        elif len(num) == 6 and len(setNum.intersection(values[4])) == len(values[4]):
            numValue = 9
        elif len(num) == 6 and len(setNum.intersection(values[1])) == len(values[1]):
            numValue = 0
        else:
            numValue = 6

        result = result * 10 + numValue
    return result


firstPartAnswer = 0
secondPartAnswer = 0
for line in f:
    first, second = getCurrentLineNums(line)
    num = getNum(first, second)
    firstPartAnswer += str(num).count('1') + str(num).count('4') + \
        str(num).count('7') + str(num).count('8')
    secondPartAnswer += num

print(firstPartAnswer, secondPartAnswer)
