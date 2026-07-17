class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        p=[]
        mx=0
        for x in nums:
            mx=max(mx,x)
            p.append(gcd(x,mx))
        p.sort()
        ans=0
        l,r=0,len(p)-1
        while l<r:
            ans+=gcd(p[l],p[r])
            l+=1
            r-=1
        return ans