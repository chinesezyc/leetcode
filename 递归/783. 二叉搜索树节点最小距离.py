# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.v1 = float('inf')
        self.v2 = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.val < self.v2:
            if root.val < self.v1:
                self.v2 = self.v1
                self.v1 = root.val
            else:
                self.v2 = root.val
        self.minDiffInBST(root.left)
        self.minDiffInBST(root.right)
        return int(self.v2 - self.v1)
