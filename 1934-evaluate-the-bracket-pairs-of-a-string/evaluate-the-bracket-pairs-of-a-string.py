class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp={key:value for key,value in knowledge}
        ans=[]
        i=0
        while i<len(s):
            if s[i]!='(':
                ans.append(s[i])
                i+=1
            else:
                j=i+1
                while s[j]!=')':
                    j+=1
                key=s[i+1:j]
                ans.append(mp.get(key,'?'))
                i=j+1
        return ''.join(ans)