class Solution:
    def lexGreaterPermutation(self, s: str, tar: str) -> str:
        n=len(s)
        cnt=[0]*26
        for ch in s:
            cnt[ord(ch)-ord('a')]+=1
        for i in range(n-1,-1,-1):
            rem=cnt.copy()
            possible=True
            for j in range(i):
                x=ord(tar[j])-ord('a')
                if rem[x]==0:
                    possible=False
                    break
                rem[x]-=1
            if not possible:
                continue
            t=ord(tar[i])-ord('a')
            for c in range(t+1,26):
                if rem[c]>0:
                    ans=tar[:i]+chr(ord('a')+c)
                    rem[c]-=1
                    for k in range(26):
                        ans+=chr(ord('a')+k)*rem[k]
                    return ans
        return ""