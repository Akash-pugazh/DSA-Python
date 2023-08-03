arr = [1, 7, 2, 1, 5, 1]
target = 7

res = list()

startPtr = 0
endPtr = 0
while endPtr < len(arr) and startPtr < len(arr):
    subArraySum = sum(arr[startPtr : endPtr + 1])
    if subArraySum == target:
        res.append([arr[startPtr : endPtr + 1]])
        if startPtr == endPtr:
            endPtr += 1
        else:
            startPtr += 1
    elif subArraySum < target:
        endPtr += 1
    elif subArraySum > target:
        startPtr += 1
print(res)
