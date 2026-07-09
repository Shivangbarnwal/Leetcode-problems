class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd=head
        even=head.next
        evenhead=even
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=evenhead
        return head
            