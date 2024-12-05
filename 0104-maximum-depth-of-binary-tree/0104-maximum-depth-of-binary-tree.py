# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        ans = 0
        q = []
        q.append(root)
        while q:
            for i in range(len(q)):
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            ans+=1
        return ans
        """
        if root is None:
            return 0
        
        c = 0
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                f = q.popleft()
                if f.left:
                    q.append(f.left)
                if f.right:
                    q.append(f.right)
            c += 1
        return c
        """
        