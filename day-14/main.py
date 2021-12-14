from collections import Counter
f = open("input.txt", "r")


def getCurrentLineNums(line):
    return line.rstrip("\n").split(" -> ")


current = f.readline().rstrip("\n")

f.readline()
rules = {}

for line in f:
    pair, add = getCurrentLineNums(line)
    rules[pair] = add


currentPairs = Counter()
for i in range(1, len(current)):
    pair = current[i-1] + current[i]
    currentPairs[pair] += 1


for i in range(40):
    nextCounter = currentPairs.copy()
    for pair in currentPairs:

        if pair not in rules:
            continue
        count = currentPairs[pair]
        add = rules[pair]

        replaceOne = pair[0] + add
        replaceTwo = add + pair[1]

        nextCounter[pair] -= count
        nextCounter[replaceOne] += count
        nextCounter[replaceTwo] += count
    currentPairs = nextCounter

countLetters = Counter()
for pair in currentPairs:
    first, second = list(pair)
    countLetters[first] += currentPairs[pair]
    countLetters[second] += currentPairs[pair]
countLetters[current[0]] += 1
countLetters[current[-1]] += 1

maxValue = 0
minValue = float("inf")
for key in countLetters:
    countLetters[key] //= 2
    maxValue = max(maxValue, countLetters[key])
    minValue = min(minValue, countLetters[key])


print(maxValue - minValue)
