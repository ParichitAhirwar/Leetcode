class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c=[0]*51
        for i in range(len(nums)-k+1):
            s=set(nums[i:i+k])
            for x in s:
                c[x]+=1
        for x in range(50,-1,-1):
            if c[x]==1:
                return x
        return -1