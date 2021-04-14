# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    sorted_list = [1, 2, 3, 4, 5]
    tmp = 0
    sum_dict = {}
    for i in sorted_list[::-1]:
        tmp += i
        sum_dict[i] = tmp

    print(sum_dict)
