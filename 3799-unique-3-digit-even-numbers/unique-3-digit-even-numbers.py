class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import Counter
        ava=Counter(digits)
        ans=0
        for num in range(100,1000,2):
            a=num//100
            b=(num//10)%10
            c=num%10
            n=Counter([a,b,c])
            if all(n[d]<=ava[d] for d in n):
                ans+=1
        return ans