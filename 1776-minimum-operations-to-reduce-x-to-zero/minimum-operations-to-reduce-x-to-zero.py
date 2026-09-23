class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        tar=sum(nums)-x
        if tar<0:
            return -1
        if tar==0:
            return n
        l=0
        cs=0
        ml=-1
        for r in range(n):
            cs+=nums[r]
            while cs>tar and l<=r:
                cs-=nums[l]
                l+=1
            if cs==tar:
                ml=max(ml,r-l+1)
        if ml==-1:
            return -1
        return n-ml