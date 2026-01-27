class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mr=0
        for i in range(len(nums)):
            if i>mr:
                return False
            mr=max(mr,i+nums[i])
        return True