class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark as visited
            dfs(i+1, j)  # Down
            dfs(i-1, j)  # Up
            dfs(i, j+1)  # Right
            dfs(i, j-1)  # Left

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1  # Found an island

        return count
