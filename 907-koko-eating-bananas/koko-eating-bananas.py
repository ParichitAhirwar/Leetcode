class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            k=(l+r)//2
            hour=0
            for p in piles:
                hour+=(p+k-1)//k
            if hour<=h:
                r=k
            else:
                l=k+1
        return l