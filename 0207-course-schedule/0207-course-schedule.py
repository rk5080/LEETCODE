class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = defaultdict(list)
        for u,v in prerequisites:
            g[v].append(u)
        v = [0]*numCourses
        for m,n in prerequisites:
            v[m]+=1
        q = []
        for i in range(numCourses):
            if v[i]==0:
                q.append(i)
        cdone = 0
        while q:
            p = q.pop(0)
            cdone += 1
            for i in g[p]:
                v[i]-=1
                if v[i]==0:
                    q.append(i)
        return numCourses==cdone
        