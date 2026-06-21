class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost=max(costs)
        count=[0]*(max_cost+1)
        for cost in costs:
            count[cost]+=1
        ans=0
        for cost in range(1,max_cost+1):
            if count[cost]==0:
                continue
            buy=min(count[cost],coins//cost)
            ans+=buy
            coins-=buy*cost
            if coins<cost:
                break
        return ans