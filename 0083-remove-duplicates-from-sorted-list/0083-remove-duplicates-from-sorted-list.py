# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        ptr=head
        nex=ptr
        while nex:
            nex=nex.next
            while nex and nex.val==ptr.val:
                nex=nex.next
            ptr.next=nex
            ptr=nex
        return head