class Solution:
    def rob(self, num: List[int]) -> int:
        if len(num)==1:
            return num[0]
        def robl(h):
            p2,p1=0,0
            for i in h:
                c=max(p1,p2+i)
                p2=p1
                p1=c
            return p1
        return max(robl(num[:-1]),robl(num[1:]))