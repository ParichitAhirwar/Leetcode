class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        mA=0
        while l<r:
            w=r-l
            mA=max(mA,min(h[l],h[r])*w)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return mA