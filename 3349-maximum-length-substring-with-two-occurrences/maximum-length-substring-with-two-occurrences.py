class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        c={}
        l=0
        ans=0
        for r in range(len(s)):
            c[s[r]]=c.get(s[r],0)+1
            while c[s[r]]>2:
                c[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans