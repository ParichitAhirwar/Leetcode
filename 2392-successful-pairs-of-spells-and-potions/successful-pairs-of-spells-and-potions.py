class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m=len(potions)
        ans=[]
        for s in spells:
            n=(success+s-1)//s
            l,r=0,m
            while l<r:
                mid=(l+r)//2
                if potions[mid]>=n:
                    r=mid
                else:
                    l=mid+1
            ans.append(m-l)
        return ans