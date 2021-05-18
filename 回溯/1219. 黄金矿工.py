from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        used = [[False] * width for _ in range(height)]
        path = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        res = 0

        def generate_next_steps(h: int, w: int):
            nonlocal path, width, height
            next_step = []
            num = 0
            for i, j in path:
                if -1 < h + i < height \
                        and -1 < w + j < width \
                        and used[h + i][w + j] is False \
                        and grid[h + i][w + j] != 0:
                    next_step.append([h + i, w + j])
                    num += 1
            return next_step, num

        def backtrace(h: int, w: int, val: int):
            nonlocal res, used
            next_step, num = generate_next_steps(h, w)
            if num == 0:
                res = max(res, val)
            else:
                for i, j in next_step:
                    used[i][j] = True
                    backtrace(i, j, val + grid[i][j])
                    used[i][j] = False

        for h in range(height):
            for w in range(width):
                if grid[h][w] != 0:
                    used[h][w] = True
                    backtrace(h, w, grid[h][w])
                    used[h][w] = False

        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]])
    print(ret)
