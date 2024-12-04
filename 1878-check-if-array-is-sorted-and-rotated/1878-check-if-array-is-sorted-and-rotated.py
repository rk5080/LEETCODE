class Solution(object):
    def check(self, nums):
        """
        Sorted = sorted(nums)
        
        for start in range(len(nums)):
            if nums[start: ] + nums[ :start] == Sorted:
                return True
        return False """
        count = 0
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            if count > 1:
                return False
        return True