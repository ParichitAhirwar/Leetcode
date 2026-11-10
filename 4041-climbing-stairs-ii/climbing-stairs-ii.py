class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=float('inf')
            for j in range(1,4):
                if i-j>=0:
                    c=dp[i-j]+costs[i-1]+j*j
                    dp[i]=min(dp[i],c)
        return dp[n]