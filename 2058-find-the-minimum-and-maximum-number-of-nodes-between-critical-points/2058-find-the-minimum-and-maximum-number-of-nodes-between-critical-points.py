# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        cur=head.next
        nex=cur.next
        initidx=-1
        latidx=-1
        i=1
        mini=float('inf')
        while nex:
            if (prev.val<cur.val and cur.val>nex.val) or (prev.val>cur.val and cur.val<nex.val):
                
                if initidx==-1:
                    initidx=i
                else:
                    mini=min(mini,i-latidx)
                latidx=i
            prev=cur
            cur=nex
            nex=nex.next
            i+=1
        if initidx==-1 or mini==float('inf'):
            return [-1,-1]
        return [mini,latidx-initidx]