class Solution:
    def minimumCost(self, c1: int, c2: int, cB: int, n1: int, n2: int) -> int:
        both=min(n1,n2)
        o1=n1*c1+n2*c2
        o2=(both*cB+(n1-both)*c1+(n2-both)*c2)
        o3=max(n1,n2)*cB
        return min(o1,o2,o3)