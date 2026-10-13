class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:abs(x))
        n=len(nums)
        k=(n+1)//2
        return sum(x*x for x in nums[n-k:])-sum(x*x for x in nums[:n-k])