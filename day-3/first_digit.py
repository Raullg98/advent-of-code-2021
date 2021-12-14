f = open("input.txt", "r")
# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
countZeroes = [0] * 12
countOnes = [0] * 12


nums = []
for x in f:
    num = x.rstrip("\n")
    nums.append(num)

gamma = ""
epsilon = ""
for i in range(12):
    for num in nums:

        digit = num[i]
        if digit == '1':
            countOnes[i] += 1
        else:
            countZeroes[i] += 1

    gamma += "0" if countZeroes[i] <= countOnes[i] else "1"
    epsilon += "1" if countZeroes[i] <= countOnes[i] else "0"
    # print(winner, countZeroes[i], countOnes[i])
    # nums = list(filter(lambda x: (x[i] == winner), nums))
    # result += winner


print(gamma, epsilon)
print(int(gamma, 2) * int(epsilon, 2))
