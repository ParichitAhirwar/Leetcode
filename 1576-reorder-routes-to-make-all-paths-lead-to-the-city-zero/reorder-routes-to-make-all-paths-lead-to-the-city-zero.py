class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))
        ans=0
        def dfs(node,parent):
            nonlocal ans
            for nei,cost in adj[node]:
                if nei==parent:
                    continue
                ans+=cost
                dfs(nei,node)
        dfs(0,-1)
        return ans