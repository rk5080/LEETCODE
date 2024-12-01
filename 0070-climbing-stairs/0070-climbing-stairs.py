class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n<=3:
            return n
        prev1 = 3
        prev2 = 2
        for i in range(4,n+1):
            c = prev1+prev2
            prev2 = prev1
            prev1 = c
        return prev1
        