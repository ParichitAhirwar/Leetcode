class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xClosest=max(x1,min(xCenter,x2))
        yClosest=max(y1,min(yCenter,y2))
        distanceSquared=((xClosest-xCenter)**2+(yClosest-yCenter)**2)
        return distanceSquared<=radius**2