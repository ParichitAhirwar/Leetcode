class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini=min(nums)
        m=0
        for n in nums:
            m+=n-mini
        return m