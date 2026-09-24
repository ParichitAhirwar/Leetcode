class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ds=sum(int(d)for d in str(nums[i]))
            if ds==i:
                return i
        return -1