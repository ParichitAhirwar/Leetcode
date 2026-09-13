class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        ans=0
        for dr in range(-(n-1),n):
            for dc in range(-(n-1),n):
                ol=0
                for r in range(n):
                    for c in range(n):
                        if img1[r][c]==1:
                            nr=r+dr
                            nc=c+dc
                            if 0<=nr<n and 0<=nc<n:
                                if img2[nr][nc]==1:
                                    ol+=1
                ans=max(ans,ol)
        return ans