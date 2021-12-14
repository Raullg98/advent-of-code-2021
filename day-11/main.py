import operator
import functools
import collections
import pprint
pp = pprint.PrettyPrinter(indent=4)
f = open("input.txt", "r")


def getCurrentLineNums(line):
    return list(map(lambda x: int(x), list(line.rstrip("\n"))))


grid = []

for line in f:
    grid.append(getCurrentLineNums(line))


m = len(grid)
n = len(grid[0])


def isValid(i, j):
    return i >= 0 and i < m and j >= 0 and j < n


directions = [(1, 1), (-1, -1), (-1, 1), (1, -1),
              (0, 1), (1, 0), (0, -1), (-1, 0)]


coords = []


def increment(grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            grid[i][j] += 1

            if grid[i][j] > 9:
                coords.append((i, j))
    return coords


steps = 1000
result = 0
for step in range(1, steps + 1):

    coords = increment(grid)
    queue = collections.deque(coords)
    seen = set(coords)

    while queue:
        i, j = queue.popleft()
        grid[i][j] = float("-inf")
        for dx, dy in directions:
            nextX = i + dx
            nextY = j + dy

            if not isValid(nextX, nextY):
                continue

            grid[nextX][nextY] += 1

            if (nextX, nextY) not in seen and grid[nextX][nextY] > 9:
                seen.add((nextX, nextY))
                queue.append((nextX, nextY))

    result += len(seen)

    for i, j in seen:
        grid[i][j] = 0

    if len(seen) == 100:
        pp.pprint(grid)
        print("STEP", step)

        break
    pp.pprint(grid)

print(result)
