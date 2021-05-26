from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix) - 1, 0
        while h >= 0 and w < len(matrix[0]):
            if matrix[h][w] == target:
                return True
            elif matrix[h][w] > target:
                h -= 1
            else:
                w += 1

        return False


if __name__ == "__main__":
    solution = Solution()
    ret = solution.searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=5)
    print(ret)
