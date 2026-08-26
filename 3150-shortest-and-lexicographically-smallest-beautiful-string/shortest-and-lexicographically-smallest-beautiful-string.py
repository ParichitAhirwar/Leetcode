class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        l=0
        o=0
        b=""
        for r in range(n):
            o+=s[r]=="1"
            while l<=r and o>=k:
                if o==k:
                    c=s[l:r+1]
                    if not b or len(c)<len(b) or (len(c)==len(b) and c<b):
                        b=c
                if s[l]=="1":
                    o-=1
                l+=1
        return b