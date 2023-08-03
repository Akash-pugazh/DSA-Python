fruits = [1, 1, 2, 3]

i = 0
j = 0
res = 0
curr = 0
hashSet = set()
while j < len(fruits):
    if fruits[j] in hashSet and len(hashSet) < 2:
        curr += 1
    if fruits[j] not in hashSet and len(hashSet) < 2:
        curr += 1
        hashSet.add(fruits[j])
    elif fruits[j] not in hashSet and len(hashSet) == 2:
        hashSet.remove(fruits[i])
        res = max(res, curr)
        curr += 1
    j += 1

print(res)
