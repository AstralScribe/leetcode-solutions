from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        new_profit = 0
        init = prices[0]
        for i in range(len(prices)):
            if prices[i] < init:
                init = prices[i]
            if prices[i] > init:
                new_profit = prices[i] - init
            if new_profit > profit:
                profit = new_profit
            
        return profit
