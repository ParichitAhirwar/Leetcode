class Solution:
    def rob(self, num: List[int]) -> int:
        if not num:
            return 0
        if len(num)==1:
            return num[0]
        p2,p1=0,0
        for i in num:
            c=max(p1,p2+i)
            p2=p1
            p1=c
        return p1