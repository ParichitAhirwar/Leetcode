class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=0
        for i in nums:
            if i!=0:
                nums[n]=i
                n+=1
        while n<len(nums):
            nums[n]=0
            n+=1