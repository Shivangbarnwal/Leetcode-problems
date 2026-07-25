# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(node):
            if not node or node==p or node==q:
                return node
            if p.val<node.val and q.val<node.val:
                return check(node.left) 
            if p.val>node.val and q.val>node.val:
                return check(node.right) 
            left=check(node.left)
            right=check(node.right)
            if not left:
                return right
            elif not right:
                return left
            return node
        return check(root)