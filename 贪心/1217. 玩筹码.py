from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a = 0
        for i in position:
            if i & 1:
                a += 1
        return min(a, len(position) - a)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.minCostToMoveChips([2, 2, 2, 3, 3])
    print(ret)
