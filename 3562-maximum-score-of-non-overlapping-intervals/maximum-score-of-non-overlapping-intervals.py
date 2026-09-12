class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        a=[
            (r,l,w,i)
            for i,(l,r,w) in enumerate(intervals)
        ]
        a.sort()
        rights=[x[0] for x in a]
        prev=[0]*n
        for i in range(n):
            right,left,weight,idx=a[i]
            prev[i]=bisect_left(rights,left,0,i)
        dp=[[(0,[]) for _ in range(5)] for _ in range(n+1)]
        def better(x,y):
            if x[0]!=y[0]:
                return x if x[0]>y[0] else y
            return x if x[1]<y[1] else y
        for i in range(1,n+1):
            right,left,weight,idx=a[i-1]
            for k in range(5):
                best=dp[i-1][k]
                if k>0:
                    score,indices=dp[prev[i-1]][k-1]
                    take=(
                        score+weight,
                        sorted(indices+[idx])
                    )
                    best=better(best,take)
                dp[i][k]=best
        return dp[n][4][1]