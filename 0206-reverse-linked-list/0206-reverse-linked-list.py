# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        node=head
        prev=None
        if not head:
            return None
        while node:
            new=node.next
            node.next=prev
            prev=node
            node=new
        return prev

        