class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD=10**9+7
        even=1
        odd=0
        ans=0
        p=0
        for n in arr:
            p^=(n%2)
            if p==1:
                ans+=even
                odd+=1
            else:
                ans+=odd
                even+=1
        return ans%MOD