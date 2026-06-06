class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        cs=""
        cn=0
        for char in s:
            if char.isdigit():
                cn=cn*10+int(char)
            elif char=='[':
                st.append((cs,cn))
                cs=""
                cn=0
            elif char==']':
                ps,n=st.pop()
                cs=ps+n*cs
            else:
                cs+=char
        return cs