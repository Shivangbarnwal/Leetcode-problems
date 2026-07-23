# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a=[]
        st=[root]
        if not root:
            return []
        while st:
            temp=[]
            fi=[]
            for j in st:
                if j:
                    fi.append(j.val)
                    if j.left:
                        temp.append(j.left)
                    if j.right:
                        temp.append(j.right)
            st=temp
            a.append(fi)
        return a
            