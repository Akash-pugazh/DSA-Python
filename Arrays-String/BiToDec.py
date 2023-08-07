binaryInput = "0000001"
# TODO : Leading zeros Fix
# binaryInput = "Oo" + binaryInput

temp = list(reversed([char for char in binaryInput]))

res = 0
for i in range(0, len(temp)):
    if temp[i] == "1":
        res += 2**i

print(temp)
print(res)
