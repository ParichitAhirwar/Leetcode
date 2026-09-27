class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        c=[]
        for ch in s:
            if ch=='(':
                st.append(c)
                c=[]
            elif ch ==')':
                c.reverse()
                c=st.pop()+c
            else:
                c.append(ch)
        return ''.join(c)