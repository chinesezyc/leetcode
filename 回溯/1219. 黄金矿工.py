from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        used = [[False] * width for _ in range(height)]
        path = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        res = []

        def check_good_path(w: int, h: int):
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

        def backtrace(w: int, h: int, val: int):
            nonlocal res, used
            tmp, num = check_good_path(w, h)
            if num == 0:
                res.append(val)
            for i, j in tmp:
                if used[i][j] or grid[i][j] == 0:
                    continue
                val += grid[i][j]
                used[i][j] = True
                backtrace(i, j, val)
                val -= grid[i][j]
                used[i][j] = False

        for h in range(height):
            for w in range(width):
                if grid[h][w] != 0:
                    used[h][w] = True
                    backtrace(w, h, grid[h][w])
                    used[h][w] = False

        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.getMaximumGold(grid=[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])
    print(ret)
