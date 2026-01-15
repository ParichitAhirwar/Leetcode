class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        eS=n*(n+1)//2
        aS=sum(nums)
        return eS-aS