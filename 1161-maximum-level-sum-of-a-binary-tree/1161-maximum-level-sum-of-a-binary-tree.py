# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        arr=[]
        def noobie(arr,lev,node):
            if len(arr)==lev:
                arr.append(node.val)
            else:
                arr[lev]+=node.val
            if node.left:
                noobie(arr,lev+1,node.left)
            if node.right:
                noobie(arr,lev+1,node.right)
        noobie(arr,0,root)
        return arr.index(max(arr))+1
