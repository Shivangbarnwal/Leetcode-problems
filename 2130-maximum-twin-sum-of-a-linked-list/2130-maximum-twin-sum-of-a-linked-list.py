# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        if not head:
            return 0
        
        ar=[]
        ptr=head
        while ptr.next:
            a=ptr.val
            ar.append(a)
            ptr=ptr.next
        ar.append(ptr.val)
        n=len(ar)
        p=list(ar)
        for i in range(len(ar)/2):
            ar[i]=ar[i]+ar[n-1-i]
        m=max(ar)
        return m

        