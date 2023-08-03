strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

hashMap = {}

for element in strs:
    count = [0] * 26
    for char in element:
        count[ord(char) - ord("a")] += 1
    if hashMap.get(tuple(count)) == None:
        hashMap[tuple(count)] = [element]
    else:
        hashMap[tuple(count)].append(element)

print(list(hashMap.values()))
