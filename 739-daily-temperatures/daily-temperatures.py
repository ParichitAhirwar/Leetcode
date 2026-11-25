class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        n=len(t)
        ans=[0]*n
        st=[]
        for i in range(n):
            while st and t[i]>t[st[-1]]:
                prev=st.pop()
                ans[prev]=i-prev
            st.append(i)
        return ans