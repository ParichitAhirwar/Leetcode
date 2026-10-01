class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        pair={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in '([{':
                st.append(ch)
            else:
                if not st or st.pop()!=pair[ch]:
                    return False
        return len(st)==0