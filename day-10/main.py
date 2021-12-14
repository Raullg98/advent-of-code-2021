import operator
import functools
f = open("input.txt", "r")


def getCurrentLineNums(line, separator=','):
    return list(line.rstrip("\n"))


values = []


for line in f:
    current = []
    for value in getCurrentLineNums(line):
        current.append(int(value))
    values.append(current)
    print(current)

m = len(values)
n = len(values[0])


def isValid(i, j):
    return i >= 0 and i < m and j >= 0 and j < n


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


coords = []
for i in range(len(values)):
    for j in range(len(values[i])):

        isInvalid = False
        for dx, dy in directions:
            nextX = i + dx
            nextY = j + dy

            if not isValid(nextX, nextY):
                continue

            if values[i][j] >= values[nextX][nextY]:
                isInvalid = True

        if not isInvalid:
            coords.append([i, j])


def dfs(i, j, seen):
    print(i, j)
    result = 1
    if (i, j) in seen:
        return 0

    if values[i][j] == 9:
        return 0

    seen.add((i, j))

    # print(values[i][j])

    for dx, dy in directions:
        nextX = i + dx
        nextY = j + dy

        if not isValid(nextX, nextY):
            continue

        if values[nextX][nextY] == 9:
            continue

        if values[nextX][nextY] < values[i][j]:
            continue

        result += dfs(nextX, nextY, seen)
    values[i][j] = 9
    return result


result = []

# print(dfs(2, 2, set()))
for i, j in coords:
    # print("alo")
    ans = dfs(i, j, set())
    result.append(ans)
    # print(ans, i, j)
# print(itertools.product())
print(functools.reduce(operator.mul, sorted(result)[-3:], 1))
