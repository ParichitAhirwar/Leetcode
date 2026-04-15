class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n=len(nums)
        tE=sum(nums[i] for i in range(0,n,2))
        tO=sum(nums[i] for i in range(1,n,2))
        lE=0
        lO=0
        res=0
        for i in range(n):
            if i%2==0:
                tE-=nums[i]
            else:
                tO-=nums[i]
            nE=lE+tO
            nO=lO+tE
            if nE==nO:
                res+=1
            if i%2==0:
                lE+=nums[i]
            else:
                lO+=nums[i]
        return res