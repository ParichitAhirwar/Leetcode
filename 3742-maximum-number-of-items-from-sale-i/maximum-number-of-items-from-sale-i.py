class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        mp=min(p for factor,p in items)
        g=[1]*n
        for i in range(n):
            for j in range(n):
                if i!=j and items[j][0]%items[i][0]==0:
                    g[i]+=1

        NEG=float('-inf')
        dp=[NEG]*(budget+1)
        dp[0]=0
        for i in range(n):
            p=items[i][1]
            for c in range(budget,p-1,-1):
                dp[c]=max(dp[c],dp[c-p]+g[i])
        ans=0
        for c in range(budget+1):
            if dp[c]!=NEG:
                extra=(budget-c)//mp
                ans=max(ans,dp[c]+extra)
        return ans