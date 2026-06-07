class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy_cost=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            cost=prices[i]- min_buy_cost
            max_profit=max(max_profit,cost)
            min_buy_cost=min(min_buy_cost,prices[i])
        return max_profit
            
        