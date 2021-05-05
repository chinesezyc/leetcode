import sys
from typing import List
import numpy as np


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w, h = len(board), len(board[0])
        flags = np.zeros(shape=(w, h), dtype=np.int)
        board_ = np.zeros(shape=(w, h), dtype=np.int)
        for i in range(w):
            for j in range(h):
                board_[i, j] = ord(board[i][j])

        def backtrace(trace: str, w: int, h: int, idx: int) -> bool:
            nonlocal flags, board_
            if trace == word:
                return True
            if board_[w, h] == ord(trace[-1]):
                for m in [-1, 1]:
                    for n in [-1, 1]:
                        if board_[w + m, h + n] == ord(word[idx]):
                            trace += word[m]
                            backtrace(trace, w + m, h + n, idx + 1)
                            trace = trace[:-1]

        for i in range(w):
            for j in range(h):
                if board_[i, j] == ord(word[0]):
                    flags[i, j] = 1
                    if backtrace(word[0], i, j, 1):
                        return True

        return False


if __name__ == "__main__":
    solution = Solution()
    ret = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
    print(ret)
