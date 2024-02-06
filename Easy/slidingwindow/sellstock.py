class Solution:
    def maxProfit(self, prices):
        buyDay = 0  # Index for the day to buy the stock
        sellDay = 1  # Index for the day to sell the stock
        maximumProfit = 0  # Maximum profit that can be achieved

        while sellDay < len(prices):
            # Profit if sold on 'sellDay'
            profitIfSoldToday = prices[sellDay] - prices[buyDay]

            if prices[buyDay] < prices[sellDay]:
                maximumProfit = max(profitIfSoldToday, maximumProfit)
            else:
                buyDay = sellDay  # Update buyDay to the current day as it has lower price

            sellDay += 1  # Move to the next day to check selling price

        return maximumProfit

    def maxProfit2(self, prices):
        min_price = float('inf')  # Initialize to positive infinity
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                potential_profit = price - min_price
                if potential_profit > max_profit:
                    max_profit = potential_profit

        return max_profit
