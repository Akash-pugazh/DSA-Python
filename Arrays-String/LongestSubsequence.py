nums = [0, -1]

hashSet = set(nums)
res = []
for number in hashSet:
    if (number - 1) not in hashSet:
        length = 1
        while (number + 1) in hashSet:
            length += 1
            number += 1
        res.append(length)

print(max(res))

# maxNums = max(nums)

# initialArr = [0] * (maxNums + 1)

# for num in nums:
#     initialArr[num] = 1

# print(initialArr)

# resultArr = []
# result: int = 0

# for value in initialArr:
#     if value == 0:
#         result = 0
#     if value == 1:
#         # result += 1

# for index, value in enumerate(initialArr):
#     if value == 1:
#         result += 1
#     elif value == 0 and initialArr[index - 1]:
#         resultArr.append(result)
#         result = 0

# else:
#     resultArr.append(result)


# print(max(resultArr))
