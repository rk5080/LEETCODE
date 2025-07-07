class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ma = 0
        d = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>ma:
                ma = prices[i]
            elif prices[i]<ma:
                d = max(d,ma-prices[i])
        return d
        """
        ma = 0
        mi = prices[0]
        for i in prices:
            if i<mi:
                mi = i
            elif i>mi:
                ma = max(ma,i-mi)
        return ma
        """