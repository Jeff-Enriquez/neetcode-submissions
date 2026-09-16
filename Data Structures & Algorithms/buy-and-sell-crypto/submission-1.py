class Solution:
    """Solver for the best time to buy and sell stock problem."""

    def maxProfit(self, prices: list[int]) -> int:
        """Calculate the maximum profit from a single buy-sell transaction.

        Uses a two-pointer approach to track the minimum buying price seen so far
        and computes the potential profit at each step.

        Args:
            prices: list of stock prices where each element represents
                the price on a given day.

        Returns:
            The maximum profit achievable. Returns 0 if no profit is possible.
        """
        max_profit: int = 0
        buy_index: int = 0
        sell_index: int = 1
        while sell_index < len(prices):
            max_profit = max(max_profit, prices[sell_index] - prices[buy_index])
            if prices[sell_index] < prices[buy_index]:
                buy_index = sell_index
            sell_index += 1
        return max_profit