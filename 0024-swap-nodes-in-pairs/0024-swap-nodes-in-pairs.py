# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        if not head:
            return None
        if not head.next:
            return head
        ptr=head
        head=head.next
        ptr.next=ptr.next.next
        head.next=ptr
        while ptr.next and ptr.next.next:
            cur=ptr.next
            new=cur.next
            cur.next=new.next
            new.next=cur
            ptr.next=new
            ptr=cur
        return head