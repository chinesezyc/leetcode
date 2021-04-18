# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        queue = [[root, 0]]
        max_length = 0
        res = []
        while queue:
            node, length = queue.pop(-1)

            if node:
                res.append(node.val)
                max_length = max(max_length, length)
                queue.append([node.right, length + 1])
                queue.append([node.left, length + 1])
            else:
                res.append(None)
        print(res)
