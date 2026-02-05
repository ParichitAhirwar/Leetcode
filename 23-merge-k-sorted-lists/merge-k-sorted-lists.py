# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    import heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap,(lst.val,i,lst))
        d=ListNode(0)
        c=d
        while heap:
            val,i,node=heapq.heappop(heap)
            c.next=node
            c=c.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return d.next