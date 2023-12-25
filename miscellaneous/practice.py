class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(matrix-1)

        while (left <= right):
            midarray = left+(right-left)//2
            if target in matrix[midarray]:
                return True
            elif matrix[midarray] < target:
                left = midarray + 1
            else:
                right = midarray - 1
            return False
