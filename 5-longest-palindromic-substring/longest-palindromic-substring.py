class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        st=0
        ml=0
        def eac(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        for i in range(len(s)):
            l1=eac(i,i)
            l2=eac(i,i+1)
            cm=max(l1,l2)
            if cm>ml:
                ml=cm
                st=i-(cm-1)//2
        return s[st:st+ml]