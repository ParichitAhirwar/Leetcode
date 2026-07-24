class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        v=[False]*n

        def dfs(r):
            v[r]=True
            for k in rooms[r]:
                if not v[k]:
                    dfs(k)
        dfs(0)
        return all(v)