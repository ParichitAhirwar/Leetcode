class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        for ch in s:
            if ch=='(':
                st.append(0)
            else:
                i=st.pop()
                if i==0:
                    sc=1
                else:
                    sc=2*i
                st[-1]+=sc
        return st[0]