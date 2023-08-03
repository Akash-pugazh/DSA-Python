s = "abcabcbb"

hashTable = {}
startPtr = 0
maxLength = 0

for endPtr in range(len(s)):
    char = s[endPtr]
    if char in hashTable and startPtr <= hashTable[char]:
        startPtr = hashTable[char] + 1
    else:
        maxLength = max(maxLength, (endPtr - startPtr) + 1)
    hashTable[char] = endPtr

print(maxLength)
