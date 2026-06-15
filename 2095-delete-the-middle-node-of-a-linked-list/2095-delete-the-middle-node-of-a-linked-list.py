# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return
        slow=head
        fast=head.next
        while fast.next:
            fast=fast.next
            if fast.next:
                fast=fast.next
                slow=slow.next
        slow.next=slow.next.next
        return head
        