# array of prices
# prices[i ] is price of a given stock on that ith day
# we maximize profit by choosing one day to buy and one day to sell

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
