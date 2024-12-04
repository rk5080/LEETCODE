
"""class Solution(object):
    def rotate(self, nums, k):
    
      # :type nums: List[int]
      # :type k: int
      # :rtype: None Do not return anything, modify nums in-place instead.

        for i in range(k):
            nums.insert(0,nums.pop())
        print(nums)

       #     for j in range(len(nums)-1,0,-1):
        #        temp=nums[j]
        #        nums[j]=nums[j-1]
        #        nums[j-1]=temp
        #print(nums)
"""

class Solution:
    def rotate(self, nums, k):
        
        n = len(nums)
        k %= n  # In case k is larger than n
        
        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Reverse the entire array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the remaining n - k elements
        reverse(k, n - 1)
    """
class Solution:
    def rotate(self, a, k):
        n = len(a)
        p=0
        while p<k:
            l = a[n-1]
            for i in range(n-1,0,-1):
                a[i] = a[i-1]
            a[0] = l
            p+=1
        return a
        """