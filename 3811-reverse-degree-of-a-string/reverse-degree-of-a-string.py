class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i,ch in enumerate(s):
            rv=26-(ord(ch)-ord('a'))
            ans+=rv*(i+1)
        return ans