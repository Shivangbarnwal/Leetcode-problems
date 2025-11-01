# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        check=set(nums)
        while cur!=None and (cur.val in check):
            cur=cur.next
        if cur is None:
            return None
        head=cur
        ptr=cur
        while ptr.next :
            if (ptr.next.val in check):
                ptr.next=ptr.next.next
                
            else:
                ptr=ptr.next
        return head
        