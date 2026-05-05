# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def rotateRight(self, head, k):
        if not head or k==0:
            return head 


        current=head
        length=0
        while current:
            length+=1
            current=current.next
        if k==length:
            return head
        k=k%length
        
        if k==0:
            return head

        for i in range(k):
            cur=head
            pre=cur
            while cur.next!=None:
                pre=cur
                cur=cur.next

            pre.next=None
            cur.next=head
            head=cur
        return head
            
