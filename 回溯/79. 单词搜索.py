from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board), len(board[0])

        def backtrace(trace: str, w: int, h: int, idx: int) -> bool:
            nonlocal width, height
            if trace == word:
                return True
            for m, n in [[-1, 0], [1, 0], [0, -1], [0, 1], ]:
                if 0 <= w + m < width \
                        and 0 <= h + n < height \
                        and board[w + m][h + n] == word[idx] \
                        and board[w + m][h + n] != '0':
                    board[w + m][h + n] = '0'
                    trace += word[idx]
                    if backtrace(trace, w + m, h + n, idx + 1):
                        return True
                    trace = trace[:-1]
                    board[w + m][h + n] = word[idx]
            return False

        for i in range(width):
            for j in range(height):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = '0'
                    if backtrace(word[0], i, j, 1):
                        return True
                    board[i][j] = tmp
        return False


if __name__ == "__main__":
    solution = Solution()
    ret = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS")
    print(ret)
