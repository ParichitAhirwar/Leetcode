class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ci={}
        ml=0
        st=0
        for e,c in enumerate(s):
            if c in ci and ci[c]>=st:
                st=ci[c]+1
            ci[c]=e
            ml=max(ml,e-st+1)
        return ml