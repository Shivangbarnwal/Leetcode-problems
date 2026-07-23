# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        def h(node):
            l=0
            r=0
            if node.left:
                l=h(node.left)
            if node.right:
                r=h(node.right)

            return 1+max(l,r)
        return h(root)