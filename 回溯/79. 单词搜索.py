import sys
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []

        def backtrace(trace: str):
            pass

        backtrace('')
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
    print(ret)
