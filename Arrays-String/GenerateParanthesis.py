def generateParenthesis(n: int):
    def backTrack(res, currString, openCount, closeCount, maxCount):
        if len(currString) == maxCount * 2:
            res.append(currString)
        if openCount < maxCount:
            backTrack(res, currString + "(", openCount + 1, closeCount, maxCount)
        if closeCount < openCount:
            backTrack(res, currString + ")", openCount, closeCount + 1, maxCount)

    res = []
    backTrack(res, "", 0, 0, n)
    return res
