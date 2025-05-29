class Solution:
    def subsets(self, nums):
        def dfs(nums, index, ans, cur):            
            if index == len(nums):  
                ans.append(cur)
            else:
                dfs(nums, index+1, ans, cur)
                dfs(nums, index+1, ans, cur+[nums[index]])
                
        ans = []
        dfs(nums, 0, ans, [])
        return ans