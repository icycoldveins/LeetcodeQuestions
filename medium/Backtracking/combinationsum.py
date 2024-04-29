class Solution:
    def combinationSum(self, candidates, target):
        # This function will be called recursively to explore all possibilities
        def backtrack(remaining, combination, start):
            if remaining == 0:
                # If we've hit the target, add a copy of the combination to the result
                result.append(list(combination))
                return
            elif remaining < 0:
                # If we've exceeded the target, there's nothing more to explore
                return

            # Loop through the candidates, starting from the current position
            for i in range(start, len(candidates)):
                # Add the current candidate to the combination
                combination.append(candidates[i])
                # Recursively try to find combinations from the current candidate onwards
                backtrack(remaining - candidates[i], combination, i)
                # Backtrack: remove the last element added and try the next candidate
                combination.pop()

        result = []
        backtrack(target, [], 0)
        return result
    # neetcodes solution
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
                       