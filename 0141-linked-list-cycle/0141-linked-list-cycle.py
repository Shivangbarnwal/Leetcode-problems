# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=slow
        if not head:
            return False
        while fast.next:
            
            slow=slow.next
            if fast.next.next:
                fast=fast.next.next
            else:
                return False
            if fast==slow:
                return True
        return False
