from typing import List, Dict

nums: List[int] = [1, 1, 1, 2, 2, 3]

k: int = 2

hash = {}
freq = [[] for _ in range(len(nums) + 1)]

for number in nums:
    hash[number] = 1 + hash.get(number, 0)
for number, count in hash.items():
    freq[count].append(number)

print(freq)

print(hash)

res = []
br = False
for i in range(len(freq) - 1, -1, -1):
    for number in freq[i]:
        res.append(number)
        if len(res) == k:
            br = True
            break
    if br:
        break
print(res)

# for number in nums:
#     if hash.get(number) == None:
#         hash[number] = 1
#     else:
#         hash[number] += 1

# temp: List[int] = []

# hashValues = list(hash.values())
# hashValues.sort(reverse=True)
# k = 2

# res = []
# for _ in range(k):
#     result = [k for k, v in hash.items() if v == hashValues[_]]
#     res.append(result[0])

# print(res)
