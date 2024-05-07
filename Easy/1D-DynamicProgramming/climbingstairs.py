class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n):
            one, two = two, one + two
        return one
