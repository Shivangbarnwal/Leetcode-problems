# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def check(root,p,q):
            if root==None or root==p or root==q:
                return root
            left=check(root.left,p,q)
            right=check(root.right,p,q)
            if left==None:
                return right
            elif right==None:
                return left
            else:
                return root
        return check(root,p,q)

        