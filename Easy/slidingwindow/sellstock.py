class Solution:
    def maxProfit(self, prices):
        buyDay = 0  # Index for the day to buy the stock
        sellDay = 1  # Index for the day to sell the stock
        maximumProfit = 0  # Maximum profit that can be achieved

        while sellDay < len(prices):
            profitIfSoldToday = prices[sellDay] - prices[buyDay]  # Profit if sold on 'sellDay'

            if prices[buyDay] < prices[sellDay]:
                maximumProfit = max(profitIfSoldToday, maximumProfit)
            else:
                buyDay = sellDay  # Update buyDay to the current day as it has lower price

            sellDay += 1  # Move to the next day to check selling price

        return maximumProfit
