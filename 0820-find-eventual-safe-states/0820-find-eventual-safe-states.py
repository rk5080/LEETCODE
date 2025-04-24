class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        #reverse the given graph connection direction to be able to do Toplogical Sort
        rg = [[] for i in range(len(graph))]
        v = [0]*len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                rg[j].append(i)
                v[i]+=1
        q = deque()
        for i in range(len(graph)):
            if v[i]==0:
                q.append(i)
        ans = []
        while q:
            p = q.popleft()
            ans.append(p)
            for i in rg[p]:
                v[i]-=1
                if v[i]==0:
                    q.append(i)
        return sorted(ans)
        