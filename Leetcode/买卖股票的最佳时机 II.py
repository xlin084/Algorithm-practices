class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        for i in range(len(prices) - 1):
            if (prices[i] < prices[i+1]):
                profit += prices[i+1] - prices[i]

        return profit

test = Solution()
# stock = [7,1,5,3,6,4]
stock = [1,2,3,4,5]
current_profit = test.maxProfit(stock)
print(current_profit)