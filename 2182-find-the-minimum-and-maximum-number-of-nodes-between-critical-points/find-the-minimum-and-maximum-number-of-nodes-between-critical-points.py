# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p=head
        c=head.next
        f=-1
        l=-1
        md=float('inf')
        i=1

        while c.next is not None:
            n=c.next
            ic=(
                (c.val>p.val and c.val>n.val) or
                (c.val<p.val and c.val<n.val)
            )
            if ic:
                if f==-1:
                    f=i
                else:
                    md=min(md,i-l)
                l=i
            p=c
            c=n
            i+=1
        if f==l:
            return [-1,-1]
        return [md,l-f]