class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        pq = []
        for i in nums:
            heapq.heappush(pq,-(i))
        f = k-1
        while f>0:
            heapq.heappop(pq)
            f -= 1
        return -pq[0]
