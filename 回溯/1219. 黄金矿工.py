from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        tiles_list = [0] * 26
        for c in tiles:
            tiles_list[ord(c) - 65] += 1
        res = 0

        def backtrace():
            nonlocal tiles_list, res

            for i in range(26):
                if tiles_list[i] == 0:
                    continue
                tiles_list[i] -= 1
                res += 1
                backtrace()
                tiles_list[i] += 1

        backtrace()
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]])
    print(ret)
