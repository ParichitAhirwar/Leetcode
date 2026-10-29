class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res=[]

        def backtrack(start,path,rem):
            if len(path)==k:
                if rem==0:
                    res.append(path[:])
                return
            for num in range(start,10):
                if num>rem:
                    break
                path.append(num)
                backtrack(num+1,path,rem-num)
                path.pop()
        backtrack(1,[],n)
        return res