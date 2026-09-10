# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0
        def dfs(node):
            if not node:
                return 0,0
            ls,lc=dfs(node.left)
            rs,rc=dfs(node.right)
            ts=node.val+ls+rs
            tc=1+lc+rc
            if node.val==ts//tc:
                self.ans+=1
            return ts,tc
        dfs(root)
        return self.ans