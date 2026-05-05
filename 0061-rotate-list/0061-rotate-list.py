# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def rotateRight(self, head, k):
        if not head or k==0:
            return head
        length=0
        cur=head
        while cur:
            length+=1
            cur=cur.next
        if length==k:
            return head
        k=k%length
        if k==0:
            return head
        
        cur=head
        for i in range(k):
            cur=cur.next
        node=cur.next
        cur.next=None
        cur=node
        while cur and cur.next:
            cur=cur.next
        cur.next=head
        head=node
        return head
