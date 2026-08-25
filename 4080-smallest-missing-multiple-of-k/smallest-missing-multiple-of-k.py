class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=set(nums)
        m=k
        while m in n:
            m+=k
        return m