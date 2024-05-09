class Solution:
    def subsets(self, nums):
        def backtrack(start, current):
            # Add the current combination to the output
            output.append(current[:])
            for i in range(start, len(nums)):
                # Include nums[i]
                current.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, current)
                # Exclude nums[i]
                current.pop()

        output = []
        backtrack(0, [])
        return output

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res


riku = Solution()
print(riku.subsets2([1, 2, 3]))
