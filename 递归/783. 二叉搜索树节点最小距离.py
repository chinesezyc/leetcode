# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.vals = list()

    def minDiffInBST(self, root: TreeNode) -> int:
        def travels(root: TreeNode):
            if root is None:
                return
            self.vals.append(root.val)
            travels(root.left)
            travels(root.right)

        travels(root)
        self.vals.sort()
        return min([self.vals[i+1]-self.vals[i] for i in range(len(self.vals)-1)])
