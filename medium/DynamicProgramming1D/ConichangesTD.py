class Solution(object):
    def coinChange(self, coins, amount):
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
