class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num.sort()
        res=[]
        for i in range(len(num)-2):
            if i>0 and num[i]==num[i-1]:
                continue 
            l,r=i+1,len(num)-1
            while l<r:
                t=num[i]+num[l]+num[r]
                if t<0:
                    l+=1
                elif t>0:
                    r-=1
                else:
                    res.append([num[i],num[l],num[r]])
                    while l<r and num[l]==num[l+1]:
                        l+=1
                    while l<r and num[r]==num[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res