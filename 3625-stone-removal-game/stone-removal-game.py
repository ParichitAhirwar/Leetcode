class Solution:
    def canAliceWin(self, n: int) -> bool:
        st=10
        a=True
        while n>=st:
            n-=st
            a=not a
            st-=1
        return not a