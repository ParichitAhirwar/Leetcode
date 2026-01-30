class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        if not h:
            return[]
        m,n=len(h),len(h[0])
        p=set()
        a=set()
        def dfs(r,c,v):
            v.add((r,c))
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc=r+dr,c+dc
                if (0<=nr<m and 0<=nc<n and (nr,nc) not in v and h[nr][nc]>=h[r][c]):
                    dfs(nr,nc,v)
        for i in range(m):
            dfs(i,0,p)
            dfs(i,n-1,a)
        for j in range(n):
            dfs(0,j,p)
            dfs(m-1,j,a)
        return list(p & a)