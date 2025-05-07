class DisjointSet:
    def __init__(self,n):
        self.size = [1]*(n+1)
        self.parent = [i for i in range(n)]
    def findUlp(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node] = self.findUlp(self.parent[node])
        return self.parent[node]
    def UnionbySize(self,u,v):
        ulpu=self.findUlp(u)
        ulpv=self.findUlp(v)
        if ulpu==ulpv:
            return
        if self.size[ulpu]>self.size[ulpv]:
            self.parent[ulpv]=ulpu
            self.size[ulpu]+=self.size[ulpv]
        else:
            self.parent[ulpu]=ulpv
            self.size[ulpv]+=self.size[ulpu]
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        cextra=0
        ds = DisjointSet(n)
        for u,v in connections:
            if ds.findUlp(u)==ds.findUlp(v):
                cextra+=1
            else:
                ds.UnionbySize(u,v)
        croot = sum(1 for i in range(n) if ds.parent[i]==i)
        ans = croot-1
        return ans if cextra>=ans else -1