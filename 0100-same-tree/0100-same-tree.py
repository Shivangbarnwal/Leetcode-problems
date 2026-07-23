# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node1,node2):
            if (node1 and not node2) or (node2 and not node1):
                return False
            if not node1 and not node2:
                return True
            if node1.val!=node2.val:
                return False
            l=check(node1.left,node2.left)
            r=check(node1.right,node2.right)
            if not l or not r:
                return False
            return True
        return check(p,q)