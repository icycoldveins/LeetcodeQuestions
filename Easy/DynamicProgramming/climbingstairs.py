class Solution(object):
    def climbStairs(self, n):
        # Create a DP array to store the number of ways to reach each step
        dp = [0] * (n + 1)

        # There is 1 way to reach step 0 and 1 way to reach step 1
        dp[0] = 1
        dp[1] = 1

        # Use DP to calculate the number of ways for each step from 2 to n
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # The final element of the DP array will contain the number of ways to reach the top
        return dp[n]

