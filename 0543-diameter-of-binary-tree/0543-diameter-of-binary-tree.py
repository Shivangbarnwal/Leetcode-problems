# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def check(node):
            if not node:
                return 0,0
            left,maxl=check(node.left)
            right,maxr=check(node.right)
            maxi=max(maxl,maxr,1+left+right)
            return (1+max(left,right)),maxi
        ans=check(root)
        return ans[1]-1