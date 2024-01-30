class Solution(object):
    def coinChange(self, coins, amount):
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
