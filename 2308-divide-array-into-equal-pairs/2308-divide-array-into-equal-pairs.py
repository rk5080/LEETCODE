class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = Counter(nums)
        for i in d:
            if (d[i]%2)!=0:
                return False
        return True