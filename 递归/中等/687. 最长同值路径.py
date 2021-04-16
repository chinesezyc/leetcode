# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath1(self, root: TreeNode) -> int:

        def helper(node: TreeNode) -> int:
            if node is None:
                return 0
            max_val = 0
            left = helper(node.left)
            right = helper(node.right)

            if node.left and node.left.val == node.val and node.right and node.right.val == node.val:
                self.ans = max(self.ans, left + right + 2)
            if node.left and node.left.val == node.val:
                max_val = max(max_val, left + 1)
            if node.right and node.right.val == node.val:
                max_val = max(max_val, right + 1)
            self.ans = max(self.ans, max_val)
            print(self.ans, max_val)
            return max_val

        helper(root)
        return self.ans

    def longestUnivaluePath2(self, root: TreeNode) -> int:

        def helper(node: TreeNode) -> int:
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            self.ans = max(self.ans, left + right)
            return max(left, right)

        helper(root)
        return self.ans

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def helper(node: TreeNode) -> int:
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            l, r = 0, 0
            if node.left and node.left.val == node.val:
                l = left + 1
            if node.right and node.right.val == node.val:
                r = right + 1
            self.ans = max(self.ans, l + r)
            return max(l, r)

        helper(root)
        return self.ans
