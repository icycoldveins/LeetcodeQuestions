class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            # Convert 1D index back to 2D indices
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


""" 
Finding the Mid Value:

In this problem, you are given a 2D matrix where each row is sorted in non-decreasing order. The task is to find whether a target value exists in this matrix.
To perform a binary search efficiently in a sorted sequence, you need to determine the mid value. In a 1D sorted array, you calculate the mid value as (left + right) // 2, where left is the left boundary, and right is the right boundary.
Adaptation for 2D Matrix:

In the given problem, you are not working with a 1D array but a 2D matrix. However, you can still perform a binary search, but you need to map the 1D index (mid) back to the corresponding 2D row and column indices.
Mapping 1D Index to 2D Indices:

The total number of elements in the matrix is m * n, where m is the number of rows, and n is the number of columns.
When you divide a 1D index mid by the number of columns n, you get the row index. This is because it tells you how many complete rows are in mid.
When you take the remainder of mid divided by n, you get the column index. This is because it tells you the position within the current row.

 """
