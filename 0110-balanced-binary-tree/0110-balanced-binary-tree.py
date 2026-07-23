# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def h(node):
            l=0
            r=0
            if node.left:
                l=h(node.left)
            if node.right:
                r=h(node.right)
            if l>-1 and r>-1 and abs(r-l)<=1:
                return 1+max(l,r)
            return -1
        k=h(root)
        if k>=0:
            return True
        return False