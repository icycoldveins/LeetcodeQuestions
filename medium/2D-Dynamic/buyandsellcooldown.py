from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # Dictionary to store the maximum profit for state (i, buying)

        def dfs(i, buying):
            # Base case: if the index exceeds the list, no more transactions can be made
            if i >= len(prices):
                return 0
            # Return the stored result if this state has already been computed
            if (i, buying) in dp:
                return dp[(i, buying)]

            # The profit if we do nothing on this day
            cooldown = dfs(i + 1, buying)

            if buying:
                # If we are buying, calculate the cost of buying the stock on this day and continue
                buy = dfs(i + 1, not buying) - prices[i]
                # Store the maximum profit of either buying or cooling down
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # If we are selling, calculate the profit from selling and skip the next day (cooldown)
                sell = dfs(i + 2, not buying) + prices[i]
                # Store the maximum profit of either selling or cooling down
                dp[(i, buying)] = max(sell, cooldown)

            # Return the computed profit for this state
            return dp[(i, buying)]

        # Start the recursion from day 0 with the intention to buy
        return dfs(0, True)
