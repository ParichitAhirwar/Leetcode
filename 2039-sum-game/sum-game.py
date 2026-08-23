class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        diff=0
        lq=0
        rq=0
        for i in range(n//2):
            if num[i]=='?':
                lq+=1
            else:
                diff+=int(num[i])
        for i in range(n//2,n):
            if num[i]=='?':
                rq+=1
            else:
                diff-=int(num[i])
        return 2*diff+9*(lq-rq)!=0