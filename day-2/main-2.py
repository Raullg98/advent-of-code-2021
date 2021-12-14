f = open("input.txt", "r")
# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
position, depth, aim = 0, 0, 0
for x in f:
    type, num = x.rstrip("\n").split(' ')
    print(type, num)
    if type == 'forward':
        position += int(num)
        depth += aim * int(num)
    elif type == 'down':
        aim += int(num)
    else:
        aim -= int(num)
print(depth, position)
print(position * depth)
