class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """ Time Complexity:O(R x C) X (O(R) + O(C))
        q = deque()
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    q.append((i,j))
        while q:
            x,y = q.popleft()
            for i in range(C):
                if matrix[x][i]!=0:
                    matrix[x][i]=0
            for i in range(R):
                if matrix[i][y]!=0:
                    matrix[i][y]=0
        return matrix
        """
        R = len(matrix)
        C = len(matrix[0])
        col0=1
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    matrix[i][0]=0

                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0 = 0
        for i in range(1,R):
            for j in range(1,C):
                if matrix[i][j]!=0:
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(C):
                matrix[0][j]=0
        if col0==0:
            for i in range(R):
                matrix[i][0]=0
        return matrix


        