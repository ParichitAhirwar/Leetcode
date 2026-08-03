class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i]=float('-inf')
            t=0
            for k in range(3):
                if i+k<n:
                    t+=stoneValue[i+k]
                    dp[i]=max(dp[i],t-dp[i+k+1])
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        else:
            return "Tie"