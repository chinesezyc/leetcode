import sys
from typing import List
import numpy as np


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board), len(board[0])
        flags = np.zeros(shape=(width, height), dtype=np.int)
        board_ = np.zeros(shape=(width, height), dtype=np.int)
        for i in range(width):
            for j in range(height):
                board_[i, j] = ord(board[i][j])

        def backtrace(trace: str, w: int, h: int, idx: int) -> bool:
            nonlocal flags, board_, width, height
            if trace == word:
                return True
            for m, n in [[-1, 0], [1, 0], [0, -1], [0, 1], ]:
                if 0 <= w + m < width and 0 <= h + n < height:
                    if board_[w + m, h + n] == ord(word[idx]) and flags[w + m, h + n] == 0:
                        # print([w + m, h + n], chr(board_[w + m, h + n]))

                        flags[w + m, h + n] = 1
                        trace += word[idx]
                        if backtrace(trace, w + m, h + n, idx + 1):
                            return True
                        trace = trace[:-1]
                        flags[w + m, h + n] = 0
            return False

        for i in range(width):
            for j in range(height):
                if board_[i, j] == ord(word[0]):
                    flags[i, j] = 1
                    if backtrace(word[0], i, j, 1):
                        return True
                    flags[i, j] = 0
        return False


if __name__ == "__main__":
    solution = Solution()
    ret = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS")
    print(ret)
