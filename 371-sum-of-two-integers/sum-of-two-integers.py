class Solution:
    def getSum(self, a: int, b: int) -> int:
        m=0xFFFFFFFF
        while b!=0:
            c=(a&b)<<1
            a=(a^b)&m
            b=c&m
        return a if a<=0x7FFFFFFF else ~(a^m)