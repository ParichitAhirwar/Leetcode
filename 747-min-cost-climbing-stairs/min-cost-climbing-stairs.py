class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        f=cost[0]
        s=cost[1]
        for i in range(2,n):
            c=cost[i]+min(f,s)
            f=s
            s=c
        return min(f,s)