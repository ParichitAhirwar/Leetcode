class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mle=min(s+d for s,d in zip(landStartTime,landDuration))
        mwe=min(s+d for s,d in zip(waterStartTime,waterDuration))
        ans=float('inf')
        for s,d in zip(waterStartTime,waterDuration):
            ans=min(ans,max(s,mle)+d)
        for s,d in zip(landStartTime,landDuration):
            ans=min(ans,max(s,mwe)+d)
        return ans