# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        n={}
        child=set()
        for p,c,i in descriptions:
            if p not in n:
                n[p]=TreeNode(p)
            if c not in n:
                n[c]=TreeNode(c)
            if i:
                n[p].left=n[c]
            else:
                n[p].right=n[c]
            child.add(c)
        for p,_,_ in descriptions:
            if p not in child:
                return n[p]