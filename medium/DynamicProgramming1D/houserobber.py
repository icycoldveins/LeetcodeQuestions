class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0
        for stash in nums:
            newrob = max(stash + house1, house2)
            house1 = house2
            house2 = newrob
        return house2
