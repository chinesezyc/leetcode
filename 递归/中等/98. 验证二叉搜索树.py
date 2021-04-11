# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root: TreeNode, lower=float('-inf'), upper=float('inf')):
            if root is None:
                return True
            if root.val >= upper or root.val <= lower:
                return False

            return helper(root.left, lower=lower, upper=root.val) and helper(root.right, lower=root.val, upper=upper)

        return helper(root)
