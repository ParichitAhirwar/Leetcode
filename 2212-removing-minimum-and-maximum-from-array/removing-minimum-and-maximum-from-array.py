class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        minIdx=nums.index(min(nums))
        maxIdx=nums.index(max(nums))
        l=min(minIdx,maxIdx)
        r=max(minIdx,maxIdx)
        front=r+1
        back=n-l
        both=(l+1)+(n-r)
        return min(front,back,both)