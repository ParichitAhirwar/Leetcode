class Solution:
    def maxDepth(self, s: str) -> int:
        d=0
        md=0 
        for c in s:
            if c=='(':
                d+=1
                md=max(md,d)
            elif c==')':
                d-=1
        return md