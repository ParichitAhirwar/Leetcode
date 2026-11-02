class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med=nums[len(nums)//2]
        m=0
        for n in nums:
            m+=abs(n-med)
        return m