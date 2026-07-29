class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def dfs(src, dst, visited, product):
            if src == dst:
                return product

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    ans = dfs(neighbor, dst, visited, product * weight)
                    if ans != -1.0:
                        return ans

            return -1.0

        result = []

        for src, dst in queries:
            if src not in graph or dst not in graph:
                result.append(-1.0)
            else:
                visited = set()
                result.append(dfs(src, dst, visited, 1.0))

        return result