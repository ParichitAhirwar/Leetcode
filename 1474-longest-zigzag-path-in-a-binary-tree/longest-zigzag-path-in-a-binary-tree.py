# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(node,direction,length):
            if not node:
                return
            self.ans=max(self.ans,length)
            if direction=="L":
                dfs(node.right,"R",length+1)
                dfs(node.left,"L",1)
            else:
                dfs(node.left,"L",length+1)
                dfs(node.right,"R",1)
        dfs(root.left,"L",1)
        dfs(root.right,"R",1)
        return self.ans