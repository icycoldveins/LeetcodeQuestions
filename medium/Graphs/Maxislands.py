class Solution(object):
    def maxAreaOfIsland(self, grid):
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0  # Marking visited cell
            area = 1
            area += dfs(grid, i+1, j)
            area += dfs(grid, i-1, j)
            area += dfs(grid, i, j+1)
            area += dfs(grid, i, j-1)
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(grid, i, j))
        return max_area
