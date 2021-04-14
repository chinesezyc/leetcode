# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST2(self, root: TreeNode) -> TreeNode:
        sorted_list = []

        def inoder(root: TreeNode):
            if root is None:
                return
            inoder(root.left)
            sorted_list.append(root.val)
            inoder(root.right)

        inoder(root)
        tmp = 0
        sum_dict = {}
        for i in sorted_list[::-1]:
            tmp += i
            sum_dict[i] = tmp

        def helper(root: TreeNode):
            if root is None:
                return
            helper(root.left)
            root.val = sum_dict[root.val]
            helper(root.right)

        helper(root)
        return root

    def convertBST(self, root: TreeNode) -> TreeNode:
        tmp = 0

        def helper(root: TreeNode):
            nonlocal tmp
            if root is None:
                return
            helper(root.right)
            tmp += root.val
            root.val = tmp
            helper(root.left)

        helper(root)
        return root


if __name__ == '__main__':
    sorted_list = [1, 2, 3, 4, 5]
    tmp = 0
    sum_dict = {}
    for i in sorted_list[::-1]:
        tmp += i
        sum_dict[i] = tmp

    print(sum_dict)
