# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compute_height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.compute_height(root.left), self.compute_height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.compute_height(root.left) - self.compute_height(root.right)) <= 1 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)
