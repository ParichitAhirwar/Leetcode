class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(i,j):
            if i==j:
                return nums[i]
            pl=nums[i]-dp(i+1,j)
            pr=nums[j]-dp(i,j-1)
            return max(pl,pr)
        return dp(0,len(nums)-1)>=0