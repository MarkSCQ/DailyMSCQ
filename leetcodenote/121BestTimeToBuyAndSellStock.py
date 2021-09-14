class Solution:
    def maxProfit(self, prices):
        # ! result the earning
        result = 0
        # ! current lowest index in price list
        current = 0
        # ! update result by searching the current biggest and smallest points
        for i in range(1, len(prices)):
            if prices[i]-prices[current] > result:
                # ~ current biggest
                result = prices[i]-prices[current]
            elif prices[i]-prices[current] < 0:
                # ~ current smallest 
                current = i
        return result
