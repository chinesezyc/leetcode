from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = [[root, 1]]
        max_depth = -1
        res = {}
        while queue:
            node, length = queue.pop(0)
            max_depth = max(max_depth, length)
            res[length] = node.val
            if node.left:
                queue.append([node.left, length + 1])
            if node.right:
                queue.append([node.right, length + 1])

        return [res[i] for i in range(1, max_depth + 1)]


if __name__ == '__main__':
    res = [[4, 3], [5, 3], [3, 2], [2, 2], [1, 1]]
    rsv = [res[0][0]]
    pre_l = res[0][1]
    for val, l in res[1:]:
        if pre_l != l:
            pre_l = l
            rsv.append(val)
    rsv.reverse()
    print(rsv)
