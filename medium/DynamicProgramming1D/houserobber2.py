class Solution:
    def rob(self, nums):
        def rob_linear(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
