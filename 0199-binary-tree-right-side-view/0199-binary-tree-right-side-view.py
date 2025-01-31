# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        def solve(root, lvl):
        	if root:
        		if len(res)==lvl:
        			res.append(root.val)
        		solve(root.right, lvl + 1)
        		solve(root.left, lvl + 1)
        	return 

        res = []
        solve(root,0)
        return res
        
        
        """
 
        def r(root):
            recursionRight(root, 0)
        def leftsideView(root):
            recursionLeft(root, 0)
        def recursionLeft(root, level):
        # Check if the current node is None
            if not root:
                return
            if len(res1) == level:
                res1.append(root.val)
            recursionLeft(root.left, level + 1)
            recursionLeft(root.right, level + 1)
        def recursionRight(root, level):
        # Check if the current node is None
            if not root:
                return
            if len(res) == level:
                res.append(root.val)
                recursionRight(root.right, level + 1)
                recursionRight(root.left, level + 1)
        res = []
        res1 = []
        r(root)
        leftsideView(root)
        if len(res1)>len(res):
            return res+res1[len(res):]
        else:
            return res
            """
        