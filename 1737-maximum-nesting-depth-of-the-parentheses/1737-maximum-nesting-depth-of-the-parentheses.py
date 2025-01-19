class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        a = []
        for i in s:
            if i == '(':
                c += 1
                a.append(c)
            elif i == ')':
                c -= 1
            elif '(' not in s:
                return 0
        return max(a)