from typing import List, Set, Dict, Tuple, Union, Any


def replaceElements(arr: List[int]) -> List[int]:
    res = [-1 for _ in range(len(arr))]
    if len(arr) == 1:
        return res
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > res[i]:
            res[i - 1] = arr[i]
        else:
            res[i - 1] = res[i]
    return res
