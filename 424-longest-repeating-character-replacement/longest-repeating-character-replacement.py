class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        mc=0
        ml=0
        st=0
        for e in range(len(s)):
            c[s[e]]=c.get(s[e],0)+1
            mc=max(mc,c[s[e]])
            if(e-st+1)-mc>k:
                c[s[st]]-=1
                st+=1
            ml=max(ml,e-st+1)
        return ml