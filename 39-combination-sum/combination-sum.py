class Solution:
    def combinationSum(self, cand: List[int], tar: int) -> List[List[int]]:
        res=[]
        def backtrack(s,c,r):
            if r==0:
                res.append(c[:])
                return 
            if r<0:
                return 
            for i in range(s,len(cand)):
                c.append(cand[i])
                backtrack(i,c,r-cand[i])
                c.pop()
        backtrack(0,[],tar)
        return res