# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=l1
        h2=l2
        carry=0
        head=ListNode(0)
        iteraa=head
        while h1 or h2:
            v1,v2=0,0
            if h1:
                v1=h1.val
                h1=h1.next
            if h2:
                v2=h2.val
                h2=h2.next
            val=v1+v2+carry
            carry=val//10
            iteraa.next=ListNode(val%10)
            iteraa=iteraa.next
            
            
        if carry!=0:
            iteraa.next=ListNode(carry)
            iteraa=iteraa.next
        return head.next