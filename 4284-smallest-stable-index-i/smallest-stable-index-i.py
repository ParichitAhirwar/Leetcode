class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        smin=[0]*n
        smin[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            smin[i]=min(nums[i],smin[i+1])
        p=nums[0]
        for i in range(n):
            p=max(p,nums[i])
            if p-smin[i]<=k:
                return i
        return -1