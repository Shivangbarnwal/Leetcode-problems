# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        a=[]
        def trav(root,a):
            if not root:
                return
            
            if root.left:
                trav(root.left,a)
            a.append(root.val)
            if root.right:
                trav(root.right,a)
        trav(root,a)

        return a
        