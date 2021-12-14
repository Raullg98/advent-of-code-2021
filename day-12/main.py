from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter(indent=4)
f = open("input.txt", "r")


def getCurrentLineNums(line):
    return line.rstrip("\n").split("-")


graph = defaultdict(list)

for line in f:
    start, end = getCurrentLineNums(line)

    if end != "start" and start != "end":
        graph[start].append(end)

    if start != "start" and end != "end":
        graph[end].append(start)


def isSmall(current):
    return current.islower()


def dfs(current, seen, remainingSmalls):
    if current == 'end':
        return 1

    visitedSmall = False
    if isSmall(current):

        if current in seen and remainingSmalls > 0:
            remainingSmalls = 0
            visitedSmall = True
        elif current in seen:
            return 0

        seen.add(current)

    result = 0
    for nextVal in graph[current]:
        result += dfs(nextVal, seen, remainingSmalls)

    if isSmall(current) and not visitedSmall:
        seen.remove(current)
    return result


# print(graph)
pp.pprint(graph)
print("first part", dfs('start', set(), 0))
print("second part", dfs('start', set(), 1))
