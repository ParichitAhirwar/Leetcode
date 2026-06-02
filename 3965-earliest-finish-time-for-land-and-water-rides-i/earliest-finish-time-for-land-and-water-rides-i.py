class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        for ls, ld in zip(landStartTime,landDuration):
            for ws,wd in zip(waterStartTime,waterDuration):
                land_finish=ls+ld
                finish_lw=max(land_finish,ws)+wd
                water_finish=ws+wd
                finish_wl=max(water_finish,ls)+ld
                ans=min(ans,finish_lw,finish_wl)
        return ans