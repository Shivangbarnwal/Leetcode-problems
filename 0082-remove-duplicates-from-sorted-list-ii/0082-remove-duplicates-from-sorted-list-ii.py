# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fake=ListNode(101)
        fake.next=head
        temp=fake
        while temp and temp.next:
            if temp.next and temp.next.next and temp.next.val==temp.next.next.val:
                dup=temp.next.val
                while temp.next and temp.next.val==dup:
                    temp.next=temp.next.next
            else:
                temp=temp.next
        return fake.next