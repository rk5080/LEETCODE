# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        q.append(root)
        ans = []
        if not root:
            return ans
        while q:
            t = q.pop()
            ans.append(t.val)
            if t.right:
                q.append(t.right)
            if t.left:
                q.append(t.left)

        return ans
        
        
        
        
        """
        def preord(root,pro):
            if root is None:
                return
            pro.append(root.val)
            preord(root.left,pro)
            preord(root.right,pro)
        pro = []
        preord(root,pro)
        return pro
        """