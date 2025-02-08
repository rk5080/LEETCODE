class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # Floyd Warshall: No cycle, +ve, -ve weights allowed
        # FW finds shortest path bw all pairs 
        # Djisktra: shortest path bw one node to other (only +ve weights allowed)
        # Bellman Ford: same as Djisktra but -ve weights allowed.
        def fw():
            # treat each intermediate node between i,j nodes!
            # complete finding all shortest path using kth intermediate node for
            # all (i,j) pairs before moving to next one.

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
        
        def findReachable():
            ans_rc = float('inf')
            ans_city = -1
            for i in range(n):
                curr_rc = 0 #rc: reachable_count
                for j in range(n):
                    if i!= j and matrix[i][j] <= distanceThreshold: curr_rc += 1

                if curr_rc < ans_rc or (curr_rc == ans_rc and i > ans_city):
                    ans_rc = curr_rc
                    ans_city = i
            
            return ans_city

        # matrix: store path between all city pairs
        matrix = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0 #path from itself
        for s,d,l in edges:
            matrix[s][d] = l
            matrix[d][s] = l
        
        fw()
        return findReachable()