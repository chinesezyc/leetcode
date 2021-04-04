# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        vals = list()

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)

        inorder(root)
        return sum([x for x in vals if low <= x <= high])


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        vals = list()

        def inorder(root: TreeNode):
            if root is None:
                return
            if root.val >= low:
                inorder(root.left)
            if low <= root.val <= high:
                vals.append(root.val)

            if root.val <= high:
                inorder(root.right)

        inorder(root)
        return sum(vals)
