class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
        # remove duplicates:
            if i != 0 and arr[i] == arr[i - 1]:
                continue

        # moving 2 pointers:
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = arr[i] + arr[j] + arr[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [arr[i], arr[j], arr[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                # skip the duplicates:
                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1

        return ans