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

        def helper(node: TreeNode):
            if node is None:
                return 0
            return max(helper(node.left) + 1, helper(node.right) + 1)

        left_max_len = helper(root.left)
        right_max_len = helper(root.right)
        if left_max_len == right_max_len:
            return root
        elif left_max_len > right_max_len:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
