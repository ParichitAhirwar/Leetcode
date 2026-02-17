class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        m={')':'(','}':'{',']':'['}
        for c in s:
            if c in m:
                t=st.pop() if st else '#'
                if m[c]!=t:
                    return False
            else:
                st.append(c)
        return not st