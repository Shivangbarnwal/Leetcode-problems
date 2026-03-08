# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, a, b):
        dummy=ListNode(-1)
        current = dummy

        while a and b:
            if a.val<=b.val:
                current.next=a
                a=a.next
            else:
                current.next=b
                b=b.next
            current=current.next
        if a:
            current.next=a
        else:
            current.next=b
        return dummy.next