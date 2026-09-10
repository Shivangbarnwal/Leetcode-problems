# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
        def check(root):
            nonlocal count
            if not root:
                return 0,0
            lsuma,lcout=check(root.left)
            rsuma,rcout=check(root.right)
            
            tot=lsuma+rsuma+root.val
            tot_nodes=lcout+rcout+1
            if tot//tot_nodes==root.val:
                count+=1
            return tot,tot_nodes
        check(root)
        return count