from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        used = [[False] * width for _ in range(height)]
        path = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        res = []

        def check_good_path(h: int, w: int):
            nonlocal path, width, height
            tmp = []
            num = 0
            for i, j in path:
                if -1 < h + i < height \
                        and -1 < w + j < width \
                        and used[h + i][w + j] is False \
                        and grid[h + i][w + j] != 0:
                    tmp.append([h + i, w + j])
                    num += 1
            return tmp, num

        def backtrace(h: int, w: int, val: int, trace: List[int]):
            nonlocal res, used
            tmp, num = check_good_path(h, w)
            if num == 0:
                res.append(val)
            for i, j in tmp:
                if used[i][j] or grid[i][j] == 0:
                    continue
                val += grid[i][j]
                used[i][j] = True
                trace.append(grid[i][j])
                backtrace(i, j, val, trace)
                val -= grid[i][j]
                used[i][j] = False
                trace.pop(-1)

        for h in range(height):
            for w in range(width):
                if grid[h][w] != 0:
                    used[h][w] = True
                    backtrace(h, w, grid[h][w], [grid[h][w]])
                    used[h][w] = False

        return max(res)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]])
    print(ret)
