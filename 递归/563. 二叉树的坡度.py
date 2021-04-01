# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def compute_sum(root: TreeNode) -> int:
            if root is None:
                return 0
            return root.val + compute_sum(root.left) + compute_sum(root.right)

        if root is None:
            return 0
        return abs(compute_sum(root.left) - compute_sum(root.right)) \
               + self.findTilt(root.left) \
               + self.findTilt(root.right)
