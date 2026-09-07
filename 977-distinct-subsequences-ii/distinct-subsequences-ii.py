class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=[0]*26
        t=0
        for ch in s:
            i=ord(ch)-ord('a')
            n=(t+1)%MOD
            t=(t-dp[i])%MOD
            dp[i]=n
            t=(t+dp[i])%MOD
        return t