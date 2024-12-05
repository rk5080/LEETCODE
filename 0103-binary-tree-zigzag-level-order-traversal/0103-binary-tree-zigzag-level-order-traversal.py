# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        flag = True
        ans = []
        q = deque()
        q.append(root)
        while q:
            l = []
            for i in range(len(q)):
                p = q.popleft()
                l.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            if flag:
                ans.append(l)
                flag = False
            elif not flag:
                ans.append(l[::-1])
                flag = True
        return ans