class Solution:
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]  # Swap
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # Swap back

        n = len(nums)
        output = []
        backtrack()
        return output
