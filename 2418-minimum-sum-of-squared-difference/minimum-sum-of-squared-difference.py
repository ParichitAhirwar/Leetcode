class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k=k1+k2
        diff=[abs(a-b)for a,b in zip(nums1,nums2)]
        if sum(diff)<=k:
            return 0
        l,r=0,max(diff)
        while l<r:
            mid=(l+r)//2
            n=sum(max(0,d-mid)for d in diff)
            if n<=k:
                r=mid
            else:
                l=mid+1
        tar=l
        op=sum(max(0,d-tar)for d in diff)
        ans=sum(min(d,tar)**2 for d in diff)
        r=k-op
        count=sum(1 for d in diff if d>=tar and tar>0)
        ans-=min(r,count)*(2*tar-1)
        return ans