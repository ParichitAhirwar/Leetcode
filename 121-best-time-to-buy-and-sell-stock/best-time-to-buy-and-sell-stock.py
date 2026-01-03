class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=float('inf')
        maxp=0
        for p in prices :
            minp=min(minp,p)
            maxp=max(maxp,p-minp)
        return maxp