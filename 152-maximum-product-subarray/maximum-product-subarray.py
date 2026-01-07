class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxP=minP=res=nums[0]
        for i in nums[1:]:
            temp=max(i,maxP*i,minP*i)
            minP=min(i,maxP*i,minP*i)
            maxP=temp
            res=max(res,maxP)
        return res