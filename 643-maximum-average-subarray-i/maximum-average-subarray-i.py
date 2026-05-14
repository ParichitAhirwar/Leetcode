class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws=sum(nums[:k])
        ms=ws
        for i in range(k,len(nums)):
            ws+=nums[i]-nums[i-k]
            ms=max(ms,ws)
        return ms/k