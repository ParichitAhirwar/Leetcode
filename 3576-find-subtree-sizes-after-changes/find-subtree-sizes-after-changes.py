class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        children=[[] for _ in range(n)]
        for i in range(1,n):
            children[parent[i]].append(i)
        l=[-1]*26
        np=parent[:]

        def dfs1(u):
            c=ord(s[u])-ord('a')
            p=l[c]
            if p!=-1:
                np[u]=p
            l[c]=u
            for v in children[u]:
                dfs1(v)
            l[c]=p

        dfs1(0)
        nc=[[] for _ in range(n)]
        for i in range(1,n):
            nc[np[i]].append(i)
        ans=[0]*n

        def dfs2(u):
            s=1
            for v in nc[u]:
                s+=dfs2(v)
            ans[u]=s
            return s
        dfs2(0)

        return ans