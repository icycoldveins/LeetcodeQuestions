import math
from typing import List


class Solution(object):
    def coinChangeBU(self, coins, amount):
        """
        :type coins: List[int] - List of coin denominations available.
        :type amount: int - The target amount to be made up.
        :rtype: int - Minimum number of coins needed to make up 'amount'.
        """
        # Step 1: Initialize an array to store the minimum number of coins
        # needed for each amount from 0 to 'amount'.
        dp = [amount+1] * (amount + 1)

        # Initialize 'dp[0]' to 0, as no coins are needed to make up 0.
        dp[0] = 0

        # Step 2: Iterate through each amount from 1 to the given 'amount'.
        for target_amount in range(1, amount + 1):
            # Step 3: Iterate through each coin denomination.
            for coin in coins:
                # Check if the current coin can be used to make up the current amount.
                if target_amount >= coin:
                    # Update the minimum number of coins needed for 'target_amount'.
                    # We consider the minimum between the current minimum
                    # and the count of coins needed for 'target_amount - coin' plus 1.
                    dp[target_amount] = min(
                        dp[target_amount], dp[target_amount - coin] + 1)

        # Step 4: If 'dp[amount]' is still equal to 'amount + 1',
        # it means making up the amount is not possible, so return -1.
        if dp[amount] == amount+1:
            return -1

        # Step 5: Return the minimum number of coins needed to make up the given 'amount'.
        return dp[amount]


class Solution(object):
    def coinChangeTD(self, coins, amount):
        # Create a memoization dictionary to store computed results.
        memo = {}

        def dp(target_amount):
            # Check if the result for this amount is already computed.
            if target_amount in memo:
                return memo[target_amount]

            # Base case: If the target amount is 0, no coins are needed.
            if target_amount == 0:
                return 0

            # Initialize the minimum number of coins needed as a large value.
            min_coins = float('inf')

            # Iterate through each coin denomination.
            for coin in coins:
                # Check if the current coin can be used to make up the target amount.
                if target_amount >= coin:
                    # Recursively calculate the minimum number of coins needed.
                    subproblem = dp(target_amount - coin)

                    # Update the minimum number of coins.
                    if subproblem != -1:
                        min_coins = min(min_coins, subproblem + 1)

            # If min_coins is still infinity, no valid combination was found.
            # Otherwise, memoize the result and return it.
            memo[target_amount] = min_coins if min_coins != float(
                'inf') else -1
            return memo[target_amount]

        # Start the recursive process from the target amount.
        result = dp(amount)
        return result

    def coinchangeneetcode(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        return dp[amount] if dp[amount] != amount+1 else -1


class Solution:
    def bottomup(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return -1 if dp[-1] == math.inf else dp[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChangeInner(rem, cache):
            if rem < 0:
                return math.inf
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]

            cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)
            return cache[rem]

        ans = coinChangeInner(amount, {})
        return -1 if ans == math.inf else ans
