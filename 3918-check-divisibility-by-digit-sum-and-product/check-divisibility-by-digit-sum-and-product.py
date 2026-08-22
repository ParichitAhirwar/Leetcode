class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=n
        ds=0
        dp=1
        while x>0:
            d=x%10
            ds+=d
            dp*=d
            x//=10
        return n%(ds+dp)==0