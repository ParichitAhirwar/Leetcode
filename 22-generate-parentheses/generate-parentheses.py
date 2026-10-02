class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def backtrack(c,a,b):
            if len(c)==2*n:
                res.append(c)
                return
            if a<n:
                backtrack(c+"(",a+1,b)
            if b<a:
                backtrack(c+")",a,b+1)
        backtrack("",0,0)
        return res