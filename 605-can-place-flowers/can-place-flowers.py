class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        l=len(flowerbed)
        for i in range(l):
            if flowerbed[i]==0:
                le=(i==0)or(flowerbed[i-1]==0)
                re=(i==l-1)or(flowerbed[i+1]==0)
                if le and re:
                    flowerbed[i]=1
                    c+=1
            if c>=n:
                return True
        return c>=n