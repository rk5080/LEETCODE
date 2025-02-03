class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_len = len(grid)
        if grid[0][0] == 1 or grid[grid_len - 1][grid_len - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            r, c, length = queue.popleft()
            if r == grid_len - 1 and c == grid_len - 1:
                return length

            for dr, dc in neighbors:
                if (min(r + dr, c + dc) >= 0 and  max(r + dr, c + dc) < grid_len and
                    grid[r + dr][c + dc] == 0 and (r + dr, c + dc) not in visited):
                    queue.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))

        return -1
        """
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
    	grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1:
                return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
	    		if 0 <= x < n and 0 <= y < n and not grid[x][y]:
		    		grid[x][y] = 1
			    	q.append((x, y, d+1))
	    return -1
        """