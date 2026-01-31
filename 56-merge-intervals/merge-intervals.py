class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        m=[intervals[0]]
        for c in intervals[1:]:
            if c[0]<=m[-1][1]:
                m[-1][1]=max(m[-1][1],c[1])
            else:
                m.append(c)
        return m