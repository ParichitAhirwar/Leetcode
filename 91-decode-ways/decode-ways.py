class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        n=len(s)
        p2,p1=1,1
        for i in range(1,n):
            c=0
            if s[i]!='0':
                c+=p1
            td=int(s[i-1:i+1])
            if 10<=td<=26:
                c+=p2
            p2=p1
            p1=c
        return p1