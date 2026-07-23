# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if (not root.left and root.right) or (not root.right and root.left):
            return False
        def check(node1,node2):
            if (node1 and not node2) or (node2 and not node1):
                return False
            if not node1 and not node2:
                return True
            if node1.val!=node2.val:
                return False
            l=check(node1.left,node2.right)
            r=check(node1.right,node2.left)
            if not l or not r:
                return False
            return True
        return check(root.left,root.right)