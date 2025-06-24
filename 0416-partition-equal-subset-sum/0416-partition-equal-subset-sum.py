class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canPartitions(n, arr):
            # Calculate the total sum of the array elements.
            totSum = sum(arr)
            
            # If the total sum is odd, it cannot be partitioned into two equal subsets.
            if totSum % 2 == 1:
                return False
            else:
                # Calculate the target sum for each subset.
                k = totSum // 2
                
                # Initialize a boolean array 'prev' to store the results for the previous row.
                prev = [False] * (k + 1)
                prev[0] = True  # Base case: An empty subset can always achieve a sum of 0.
                
                # Handle the base case for the first element in the array.
                if arr[0] <= k:
                    prev[arr[0]] = True

                # Iterate through the elements in the array.
                for ind in range(1, n):
                    # Initialize a new boolean array 'cur' for the current row.
                    cur = [False] * (k + 1)
                    cur[0] = True  # An empty subset can always achieve a sum of 0.

                    # Fill in the 'cur' array using dynamic programming.
                    for target in range(1, k + 1):
                        # If the current element is not taken, the result is the same as the previous row.
                        notTaken = prev[target]
                        
                        # If the current element is taken, subtract its value from the target and check the previous row.
                        taken = False
                        if arr[ind] <= target:
                            taken = prev[target - arr[ind]]
                        
                        # Update the 'cur' array with the result of taking or not taking the current element.
                        cur[target] = notTaken or taken
                    
                    # Update 'prev' to 'cur' for the next iteration.
                    prev = cur
                
                # The final result is stored in 'prev[k]', indicating whether a subset with sum 'k' is possible.
                return prev[k]
        return canPartitions(len(nums), nums)
        