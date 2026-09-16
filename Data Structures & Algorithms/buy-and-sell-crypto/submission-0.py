class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit: int = 0
        l_ptr: int = 0
        r_ptr: int = 1
        while r_ptr < len(prices):
            max_profit = max(max_profit, prices[r_ptr] - prices[l_ptr])
            if prices[r_ptr] < prices[l_ptr]:
                l_ptr = r_ptr
            r_ptr += 1
        return max_profit