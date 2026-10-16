class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        a=1
        p=points[0][1]
        for start,end in points[1:]:
            if start>p:
                a+=1
                p=end
        return a