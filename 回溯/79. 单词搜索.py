import sys
from typing import List
import numpy as np


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board), len(board[0])
        board_ = np.zeros(shape=(width, height), dtype=np.int)
        for i in range(width):
            for j in range(height):
                board_[i, j] = ord(board[i][j])

        def backtrace(trace: str, w: int, h: int, idx: int) -> bool:
            nonlocal board_, width, height
            if trace == word:
                return True
            for m, n in [[-1, 0], [1, 0], [0, -1], [0, 1], ]:
                if 0 <= w + m < width \
                        and 0 <= h + n < height \
                        and board_[w + m, h + n] == ord(word[idx]) \
                        and board_[w + m, h + n] != -1:
                    tmp = board_[w + m, h + n]
                    board_[w + m, h + n] = -1
                    trace += word[idx]
                    if backtrace(trace, w + m, h + n, idx + 1):
                        return True
                    trace = trace[:-1]
                    board_[w + m, h + n] = tmp
            return False

        for i in range(width):
            for j in range(height):
                if board_[i, j] == ord(word[0]):
                    tmp = board_[i, j]
                    board_[i, j] = -1
                    if backtrace(word[0], i, j, 1):
                        return True
                    board_[i, j] = tmp
        return False


if __name__ == "__main__":
    solution = Solution()
    ret = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS")
    print(ret)
