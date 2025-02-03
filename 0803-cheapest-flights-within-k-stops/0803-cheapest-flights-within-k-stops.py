class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
        dist=[float('inf')for i in range(n)]
        dist[src]=0
        q=[[0,src,0]]   #[stops, node, toatlcost]
        while q:
            stp,node,cost=q.pop(0)  #popping from left, alternatively u you can use dequeu()
            if stp>k:
                continue
            for elm in adj[node]:
                adjnode,fcost=elm[0],elm[1]
                if dist[adjnode]>cost+fcost and stp<=k:  # <= check means we are taking into considerating all the stops, bcz we are not including the staring and the ending stops
                    dist[adjnode]=cost+fcost
                    q.append([stp+1,adjnode,cost+fcost])   #increasing one stop
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]
        """
        graph = defaultdict(list)

        for frm,to,price in flights:
            graph[frm].append((to,price))

        heap = [(0,0,src)] #price,stops,city
        visited = {}

        while heap:
            price,stops,city = heapq.heappop(heap)

            if stops>k+1:
                continue
            
            if city==dst:
                return price

            if city in visited and visited[city]==stops:
                continue

            visited[city] = stops

            for nei,p in graph[city]:
                if nei not in visited or visited[nei]>stops:
                    heapq.heappush(heap,(price+p,stops+1,nei))

        return -1
        """