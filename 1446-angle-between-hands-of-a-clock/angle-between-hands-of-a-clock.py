class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour%=12
        ha=hour*30+minutes*0.5
        ma=minutes*6
        diff=abs(ha-ma)
        return min(diff,360-diff)