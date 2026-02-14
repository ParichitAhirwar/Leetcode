class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        tc={}
        for c in t:
            tc[c]=tc.get(c,0)+1
        rq=len(tc)
        f=0
        wc={}
        l=0
        ml=float('inf')
        mw=(0,0)
        for r in range(len(s)):
            c=s[r]
            wc[c]=wc.get(c,0)+1
            if c in tc and wc[c]==tc[c]:
                f+=1
            while f==rq and l<=r:
                if r-l+1<ml:
                    ml=r-l+1
                    mw=(l,r)
                c=s[l]
                wc[c]-=1
                if c in tc and wc[c]<tc[c]:
                    f-=1
                l+=1
        return "" if ml==float('inf') else s[mw[0]:mw[1]+1]