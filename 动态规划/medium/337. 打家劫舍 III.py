from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        f, g = {None: 0}, {None: 0}

        def dfs(node: TreeNode):
            if node is None:
                return None
            dfs(node.left)
            dfs(node.right)
            f[node] = g[node.left] + g[node.right] + node.val
            g[node] = max(f[node.left], g[node.left]) + max(f[node.right], g[node.right])

        dfs(root)
        return max(f[root], g[root])
