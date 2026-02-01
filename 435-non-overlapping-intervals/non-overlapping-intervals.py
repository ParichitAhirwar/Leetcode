class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        t=float('-inf')
        for i in intervals:
            if i[0]>=t:
                t=i[1]
            else:
                c+=1
        return c