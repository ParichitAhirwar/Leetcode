class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ca=0
        ma=0
        for g in gain:
            ca+=g
            ma=max(ma,ca)
        return ma