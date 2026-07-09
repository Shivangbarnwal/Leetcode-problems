# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        t1,t2=headA,headB
        while t1!=t2:
            t1=t1.next
            t2=t2.next
            if not t1 and not t2:
                return None
            if not t1:
                t1=headB
            if not t2:
                t2=headA
             
        return t1
        
        