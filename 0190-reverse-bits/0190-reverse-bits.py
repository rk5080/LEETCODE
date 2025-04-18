class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1       # Shift left
            res += (n & 1)       # Add the least significant bit of n to res
            n = n >> 1           # Shift n to the right
        return res