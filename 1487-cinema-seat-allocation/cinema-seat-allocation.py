class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for r,s in reservedSeats:
            rows.setdefault(r,set()).add(s)
        ans=2*(n-len(rows))
        for seats in rows.values():
            if not any(s in seats for s in [2,3,4,5]):
                l=True
            else:
                l=False
            if not any(s in seats for s in [4,5,6,7]):
                m=True
            else:
                m=False
            if not any(s in seats for s in [6,7,8,9]):
                r=True
            else:
                r=False
            if l and r:
                ans+=2
            elif l or m or r:
                ans+=1
        return ans