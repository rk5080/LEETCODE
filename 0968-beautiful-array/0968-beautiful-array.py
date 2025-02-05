class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        N=n
        nums = list(range(1, N+1))
        
        def helper(nums):
            if len(nums) < 3:
                return nums
            even = nums[::2]
            odd = nums[1::2]
            return helper(even) + helper(odd)
        return helper(nums)