f = open("input.txt", "r")

nums = []
numberSize = 0
for x in f:
    num = x.rstrip("\n")
    nums.append(num)
    numberSize = len(num)


def countBits(nums, index):
    countZeroes, countOnes = 0, 0

    for num in nums:
        digit = num[index]
        if digit == '1':
            countOnes += 1
        else:
            countZeroes += 1

    return (countZeroes, countOnes)


def getBinaryValue(nums, selectWinner):
    result = ""
    for i in range(numberSize):
        countZeroes, countOnes = countBits(nums, i)
        winner = selectWinner(countZeroes, countOnes)
        nums = list(filter(lambda x: (x[i] == winner), nums))

        if len(nums) == 1:
            return nums[0]

        result += winner


oxygen = getBinaryValue(nums, lambda countZeroes,
                        countOnes: "0" if countZeroes > countOnes else "1")

co2 = getBinaryValue(nums, lambda countZeroes,
                     countOnes: "0" if countZeroes <= countOnes else "1")

print(oxygen)
print(co2)
print(int(oxygen, 2) * int(co2, 2))
