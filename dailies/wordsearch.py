class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            board[r][c] = '*'  # Mark as visited
            # Explore neighbors
            res = (dfs(r - 1, c, index + 1) or
                   dfs(r + 1, c, index + 1) or
                   dfs(r, c - 1, index + 1) or
                   dfs(r, c + 1, index + 1))
            board[r][c] = word[index]  # Revert back
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()

        def dfs(r: int, c: int, charindex: int) -> bool:
            if charindex == len(word):
                return True
            if (
                r < 0
                or c < 0
                or row <= r
                or col <= c
                or board[r][c] != word[charindex]
                or (r, c) in visited
            ):
                return False
            visited.add((r, c))
            res = (
                dfs(r + 1, c, charindex + 1)
                or dfs(r - 1, c, charindex + 1)
                or dfs(r, c + 1, charindex + 1)
                or dfs(r, c - 1, charindex + 1)
            )
            visited.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
