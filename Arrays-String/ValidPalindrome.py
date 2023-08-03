s = "A man, a plan, a canal: Panama"


def ValidPalindorme(s: str):
    temp = ""
    for char in s:
        if char.isalnum():
            temp += char.lower()
    print(temp)
    leftPtr = 0
    rightPtr = len(temp) - 1
    # ^ Two Pointers
    while leftPtr <= rightPtr:
        if temp[leftPtr] != temp[rightPtr]:
            return False
        leftPtr += 1
        rightPtr -= 1

    return True


print(ValidPalindorme(s))