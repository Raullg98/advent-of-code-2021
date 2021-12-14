from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter(indent=4)
f = open("input.txt", "r")


def getCurrentLineNums(line):
    return list(map(lambda x: int(x), line.rstrip("\n").split(",")))


maxSize = 1500
grid = [[" "] * maxSize for i in range(maxSize)]

for line in f:
    if line == '\n':
        break

    y, x = getCurrentLineNums(line)

    grid[x][y] = "#"

# pp.pprint(grid)


def flipX(grid, foldX):
    for i in range(len(grid)):
        for j in range(foldX):
            nextY = i
            nextX = foldX + (foldX - j)

            if grid[nextY][nextX] == "#":
                grid[i][j] = "#"

    for i in range(len(grid)):
        grid[i] = grid[i][:foldX]

    return grid


def flipY(grid, foldY):
    for i in range(foldY):
        for j in range(len(grid[i])):
            nextY = foldY + (foldY - i)
            nextX = j

            if grid[nextY][nextX] == "#":
                grid[i][j] = "#"

    return grid[:foldY]


def getCount(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                count += 1
    return count


# pp.pprint(grid)
# grid = flipY(grid, 7)
print("----------")

# pp.pprint(grid)
print("----------")

# fold along x = 655
# fold along y = 447
# fold along x = 327
# fold along y = 223
# fold along x = 163
# fold along y = 111
# fold along x = 81
# fold along y = 55
# fold along x = 40
# fold along y = 27
# fold along y = 13
# fold along y = 6
grid = flipX(grid, 655)
grid = flipY(grid, 447)
grid = flipX(grid, 327)
grid = flipY(grid, 223)
grid = flipX(grid, 163)
grid = flipY(grid, 111)
grid = flipX(grid, 81)
grid = flipY(grid, 55)
grid = flipX(grid, 40)
grid = flipY(grid, 27)
grid = flipY(grid, 13)
grid = flipY(grid, 6)
print("----------")


pp.pprint(grid)
for i in range(len(grid)):
    print(grid[i])
# print(getCount(grid))
