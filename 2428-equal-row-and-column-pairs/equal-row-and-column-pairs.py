class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rc=Counter(tuple(row) for row in grid)
        ans=0
        n=len(grid)
        for c in range(n):
            col=tuple(grid[r][c] for r in range(n))
            ans+=rc[col]
        return ans