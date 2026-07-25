# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def iter(node,n):
            if not node:
                return None,n
            s,n= iter(node.left,n)
            if s is not None:
                return s,n
            n+=1
            if n==k:
                return node.val,n
            return iter(node.right,n)
        return iter(root,0)[0]
            