class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd =float('inf')
        even=float('inf')
        for x in nums1:
            if x%2==1:
                odd=min(odd,x)
            else:
                even=min(even,x)
        if odd==float('inf') or even==float('inf'):
            return True
        return odd<even