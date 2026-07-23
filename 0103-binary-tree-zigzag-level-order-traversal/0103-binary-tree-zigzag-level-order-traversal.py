# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st=[root]
        ans=[]
        lav=-1
        if not root:
            return []
        while st:
            lav+=1
            temp=[]
            back=[]
            for j in st:
                temp.append(j.val)
                if j.left:
                    back.append(j.left)
                if j.right:
                    back.append(j.right)
            ans.append(temp[::(-1)**lav])
            st=back
        return ans
        