# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = list()

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)

        inorder(root)
        head = cur = TreeNode()
        for val in values:
            cur.right = TreeNode(val)
            cur = cur.right
        return head.right
