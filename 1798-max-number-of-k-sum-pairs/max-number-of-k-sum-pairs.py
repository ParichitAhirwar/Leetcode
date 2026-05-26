class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c={}
        o=0
        for n in nums:
            com=k-n
            if c.get(com,0)>0:
                o+=1
                c[com]-=1
            else:
                c[n]=c.get(n,0)+1
        return o
