class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        f=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    f+=1
        minute=0
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and f>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in d:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        f-=1
                        q.append((nr,nc))
            minute+=1
        return minute if f==0 else -1