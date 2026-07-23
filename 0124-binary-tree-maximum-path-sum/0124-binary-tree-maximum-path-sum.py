# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def check(node):
            maxl,maxr=-float('inf'),-float('inf')
            left,right=0,0
            if node.left:
                left,maxl=check(node.left)
            if node.right:
                right,maxr=check(node.right)
            left=max(0,left)
            right=max(0,right)
            maxi=max(maxl,maxr,node.val+left+right)
            b=node.val+max(left,right)
            return b,maxi
        return check(root)[1]