class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def getMiniPathSum(matrix):
            n = len(matrix)  # Number of rows
            m = len(matrix[0])  # Number of columns

            # Initialize two lists: prev (previous row) and cur (current row)
            prev = [0] * m
            cur = [0] * m

            # Initializing the first row of prev as the base condition
            for j in range(m):
                prev[j] = matrix[0][j]

            # Iterate through the matrix to compute the maximum path sum
            for i in range(1, n):
                for j in range(m):
                    # Calculate the three possible moves: up, left diagonal, and right diagonal
                    up = matrix[i][j] + prev[j]

                    leftDiagonal = matrix[i][j]
                    if j - 1 >= 0:
                        leftDiagonal += prev[j - 1]
                    else:
                        leftDiagonal += int(1e9)  # A large negative value if out of bounds

                    rightDiagonal = matrix[i][j]
                    if j + 1 < m:
                        rightDiagonal += prev[j + 1]
                    else:
                        rightDiagonal += int(1e9)  # A large negative value if out of bounds

                    # Store the maximum of the three moves in the current row (cur)
                    cur[j] = min(up, min(leftDiagonal, rightDiagonal))

                # Update prev with the values of cur for the next iteration
                prev = cur[:]

            # Find the maximum path sum in the last row of prev
            mini = sys.maxsize
            for j in range(m):
                mini = min(mini, prev[j])

            return mini
        return getMiniPathSum(matrix)