f = open("input.txt", "r")
# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
position, depth = 0, 0
for x in f:
    type, num = x.rstrip("\n").split(' ')
    print(type, num)
    if type == 'forward':
        position += int(num)
    elif type == 'down':
        depth += int(num)
    else:
        depth -= int(num)
print(depth, position)
print(position * depth)
