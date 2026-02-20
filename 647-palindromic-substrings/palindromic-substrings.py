class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        c=0
        def expand(l,r):
            nonlocal c
            while l>=0 and r<n and s[l]==s[r]:
                c+=1
                l-=1
                r+=1
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return c