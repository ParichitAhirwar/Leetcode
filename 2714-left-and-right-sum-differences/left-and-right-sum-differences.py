class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ts=sum(nums)
        ls=0
        ans=[]
        for n in nums:
            rs=ts-ls-n
            ans.append(abs(ls-rs))
            ls+=n
        return ans