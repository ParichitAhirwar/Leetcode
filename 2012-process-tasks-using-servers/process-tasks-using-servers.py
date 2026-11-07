class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n=len(servers)
        free=[(servers[i],i)for i in range(n)]
        heapq.heapify(free)
        busy=[]
        ans=[0]*len(tasks)
        time=0
        for j,task in enumerate(tasks):
            time=max(time,j)
            while busy and busy[0][0]<=time:
                available,weight,idx=heapq.heappop(busy)
                heapq.heappush(free,(weight,idx))
            if not free:
                time=busy[0][0]
                while busy and busy[0][0]<=time:
                    available,weight,idx=heapq.heappop(busy)
                    heapq.heappush(free,(weight,idx))
            weight,idx=heapq.heappop(free)
            ans[j]=idx
            heapq.heappush(busy,(time+task,weight,idx))
        return ans