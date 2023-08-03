def lengthOfLastWord(s: str) -> int:
    if len(s) == 1:
        return len(s)
    count = 0
    ptr = len(s) - 1
    while s[ptr] == " ":
        ptr -= 1
    while ptr >= 0 and s[ptr].isalpha():
        count += 1
        if ptr > 0 and s[ptr - 1] == " ":
            break
        ptr -= 1

    return count
