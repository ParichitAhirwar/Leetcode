class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        for n in nums:
            if n<pivot:
                a.append(n)
            elif n==pivot:
                b.append(n)
            else:
                c.append(n)
        return a+b+c