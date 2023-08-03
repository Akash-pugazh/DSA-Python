from typing import List, Set, Dict, Tuple, Union, Any


def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    targetStack: List[str] = [char for char in s]
    totalStack: List[str] = [char for char in t]
    for i in range(len(totalStack) - 1, -1, -1):
        totalTop: str = totalStack.pop()
        if targetStack and totalTop == targetStack[-1]:
            targetStack.pop()
    if targetStack:
        return False
    return True


s = "aec"
t = "ahbgdc"

print(isSubsequence(s, t))
