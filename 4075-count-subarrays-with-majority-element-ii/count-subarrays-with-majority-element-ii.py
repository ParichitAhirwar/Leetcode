from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.bit=[0]*(n+1)

    def update(self,i,delta):
        while i<len(self.bit):
            self.bit[i]+=delta
            i+=i&-i

    def query(self, i):
        res=0
        while i>0:
            res+=self.bit[i]
            i-=i&-i
        return res

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        pref=[0]
        s=0
        for x in nums:
            s+=1 if x==target else -1
            pref.append(s)
        vals=sorted(set(pref))
        bit=Fenwick(len(vals))
        ans=0
        for x in pref:
            idx=bisect_left(vals,x) + 1 
            ans+=bit.query(idx-1)       
            bit.update(idx,1)
        return ans