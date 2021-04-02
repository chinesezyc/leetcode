# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.val = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.minDiffInBST(root.left)
        right = self.minDiffInBST(root.right)
        self.val = min(root.val-left,root.val-right,self.val)
        return self.val
