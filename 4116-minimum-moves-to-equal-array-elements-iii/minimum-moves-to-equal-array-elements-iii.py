class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        m=0
        for n in nums:
            m+=maxi-n
        return m