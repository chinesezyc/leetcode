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

class Solution2(object):
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.tilt

    def traverse(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left-right)
        return left+right+root.val
