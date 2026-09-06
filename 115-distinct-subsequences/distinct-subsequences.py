class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(t)
        dp=[0]*(n+1)
        dp[0]=1
        for c in s:
            for j in range(n,0,-1):
                if c==t[j-1]:
                    dp[j]+=dp[j-1]
        return dp[n]