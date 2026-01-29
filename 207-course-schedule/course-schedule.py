class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[] for _ in range(numCourses)]
        for cr,pr in prerequisites:
            g[cr].append(pr)
        vi=[0]*numCourses
        def has_cycle(cr):
            if vi[cr]==1:
                return True
            if vi[cr]==2:
                return False
            vi[cr]=1
            for pr in g[cr]:
                if has_cycle(pr):
                    return True
            vi[cr]=2
            return False
        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True