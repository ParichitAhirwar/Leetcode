"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cl={}
        def dfs(node):
            if node in cl:
                return cl[node]
            c=Node(node.val)
            cl[node]=c
            for n in node.neighbors:
                c.neighbors.append(dfs(n))
            return c
        return dfs(node)