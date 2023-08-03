matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 34324


def bs(matrix, target):
    lRow, rRow = 0, len(matrix) - 1
    lCol, rCol = 0, len(matrix[0]) - 1

    while lRow <= rRow:
        # ! BS to determine row
        mRow = (lRow + rRow) // 2

        if matrix[mRow][lCol] <= target and target <= matrix[mRow][rCol]:
            # ! Binary Search to determine Col
            while lCol <= rCol:
                mCol = (lCol + rCol) // 2
                print(lCol, mCol, rCol)
                if matrix[mRow][mCol] == target:
                    return True
                elif matrix[mRow][mCol] > target:
                    rCol = mCol - 1
                else:
                    lCol = mCol + 1
        elif matrix[mRow][lCol] > target:
            rRow = mRow - 1
        else:
            lRow = mRow + 1
    return False


print(bs(matrix, target))
