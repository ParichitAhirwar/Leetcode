class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=sorted(zip(nums2,nums1),reverse=True)
        heap=[]
        cs=0
        ans=0
        for mn,n1 in pairs:
            heapq.heappush(heap,n1)
            cs+=n1
            if len(heap)>k:
                cs-=heapq.heappop(heap)
            if len(heap)==k:
                ans=max(ans,cs*mn)
        return ans