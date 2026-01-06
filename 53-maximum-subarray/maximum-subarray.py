class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mS=nums[0]
        cS=nums[0]
        for i in nums[1:]:
            cS=max(i,cS+i)
            mS=max(mS,cS)
        return mS