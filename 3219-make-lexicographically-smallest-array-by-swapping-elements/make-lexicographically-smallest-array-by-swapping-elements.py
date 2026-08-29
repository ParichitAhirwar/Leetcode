class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        pairs=sorted((v,i) for i,v in enumerate(nums))
        ans=nums[:]
        s=0
        while s<n:
            e=s
            while (e+1<n and pairs[e+1][0]-pairs[e][0]<=limit):
                e+=1
            value=[pairs[i][0] for i in range(s,e+1)]
            indices=sorted(pairs[i][1] for i in range(s,e+1))
            for idx,v in zip(indices, value):
                ans[idx]=v
            s=e+1
        return ans