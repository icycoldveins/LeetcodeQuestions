class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            option1 = dp[i - 1] + cost[i - 1]
            option2 = dp[i - 2] + cost[i - 2]
            dp[i] = min(option1, option2)

        return min(dp[n], dp[n - 1])
        