class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array (matrix) with 0's, of dimensions m x n
        dp = [[0] * n for _ in range(m)]

        # Initialize the first row and column with 1's
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                # Each cell is the sum of the cell above it and the cell to its left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Return the value at the bottom-right corner of the matrix
        return dp[-1][-1]
