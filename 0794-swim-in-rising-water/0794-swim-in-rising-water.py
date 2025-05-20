class Solution:
    def neighbors(self, grid, node):
        directions, nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1)], []
        for dx, dy in directions : 
            new_x, new_y = node[0] + dx, node[1] + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) :   
                nbrs.append((new_x, new_y))
        return nbrs 

    def swimInWater(self, grid):
        visited = {}
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                visited[(i, j)] = False 

        visited[(0, 0)] = True
        heap, max_distance = [], 0
        heappush(heap, (grid[0][0], (0, 0)))
        while heap : 
            dist, node = heappop(heap)
            if dist > max_distance : 
                max_distance = dist 
            if node == (len(grid)-1, len(grid[0])-1) : 
                return max_distance

            for nbr in self.neighbors(grid, node) :
                if not visited[nbr] : 
                    heappush(heap, (grid[nbr[0]][nbr[1]], nbr))
                    visited[nbr] = True  