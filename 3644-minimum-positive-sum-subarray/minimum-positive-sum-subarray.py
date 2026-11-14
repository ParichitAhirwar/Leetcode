class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        pf=[0]*(n+1)
        for i in range(n):
            pf[i+1]=pf[i]+nums[i]
        ans=float('inf')
        for i in range(n):
            for leng in range(l,r+1):
                j=i+leng
                if j>n:
                    break
                t=pf[j]-pf[i]
                if t>0:
                    ans=min(ans,t)
        return ans if ans!=float('inf') else -1