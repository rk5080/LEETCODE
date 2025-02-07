class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = defaultdict(list)
        for c,p in prerequisites:
            g[p].append(c)
        v = [0]*numCourses
        for c,p in prerequisites:
            v[c] += 1
        q = []
        for i in range(numCourses):
            if v[i]==0:
                q.append(i)
        ans = []
        while q:
            n = q.pop(0)
            ans.append(n)
            for i in g[n]:
                v[i]-=1
                if v[i]==0:
                    q.append(i)
        if len(ans)<numCourses:
            return []
        return ans