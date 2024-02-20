class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m, n = len(heights), len(heights[0])

        def dfs(i, j, prev_height, coords):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if (i, j) in coords:
                return
            height = heights[i][j]
            if height < prev_height:
                return
            coords.add((i, j))
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)

        pacific_coords = set()
        atlantic_coords = set()

        # DFS from top and left edges for Pacific Ocean
        for j in range(n):
            dfs(0, j, 0, pacific_coords)
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)

        # DFS from bottom and right edges for Atlantic Ocean
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)

        # Intersect sets to find cells reachable from both oceans
        return list(pacific_coords & atlantic_coords)
