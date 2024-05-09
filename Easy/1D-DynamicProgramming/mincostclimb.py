from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur = 0
        dp0 = cost[0]
        if len(cost) >= 2:
            dp1 = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur

        return min(dp0, dp1)

    def neetcode(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])

    def minCostClimbingKevin(self, cost: List[int]) -> int:
        # we have an array called cost
        # cost[i] would be the cost of the ith step
        # ex:cost[1] = 1st step
        # after paying you can climb one or two
        # start is from index 0 or index 1
        # return min cost
        # the top would be if we go over the length of cost
        for i in range(2, len(cost)):
            # cost at this index will be updated by the two previous values
            cost[i] += min([cost[i-2], cost[i-1]])
            # since we go over from the second to last or last step return min
        return min(cost[-1], cost[-2])
