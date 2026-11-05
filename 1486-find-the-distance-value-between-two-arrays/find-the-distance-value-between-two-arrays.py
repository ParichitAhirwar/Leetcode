class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c=0
        for i in arr1:
            v=True
            for j in arr2:
                if abs(i-j)<=d:
                    v=False
                    break
            if v:
                c+=1
        return c