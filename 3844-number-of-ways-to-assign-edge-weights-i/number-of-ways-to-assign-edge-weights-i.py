class Solution:
    MOD=10**9+7
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n=len(edges)+1
        graph=[[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth=[-1]*(n+1)
        depth[1]=0
        q=deque([1])
        max_depth=0
        while q:
            u=q.popleft()
            max_depth=max(max_depth,depth[u])
            for v in graph[u]:
                if depth[v]==-1:
                    depth[v]=depth[u]+1
                    q.append(v)
        return pow(2,max_depth-1,self.MOD)         