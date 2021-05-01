from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        left, right, length = 0, 0, 0

        def backtrace(trace: str):
            nonlocal left, right, length
            if length == 2 * n:
                res.append(trace)
                return

            if left < n:
                trace += '('
                left += 1
                length += 1
                backtrace(trace)
                trace = trace[:-1]
                left -= 1
                length -= 1
            if right < left:
                trace += ')'
                right += 1
                length += 1
                backtrace(trace)
                right -= 1
                length -= 1

        backtrace('')
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
    print(ret)
