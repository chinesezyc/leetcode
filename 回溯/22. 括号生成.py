from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        left, right, length = 0, 0, 0

        def backtrace(trace: str):
            nonlocal left, right, length
            if length == 2 * n:
                res.append(trace)
                return

            if right >= left and left < n:
                trace += '('
                left += 1
                length += 1
                backtrace(trace)
                trace = trace[:-1]
                left -= 1
                length -= 1
            else:
                if left < n:
                    trace += '('
                    left += 1
                    length += 1
                    backtrace(trace)
                    trace = trace[:-1]
                    left -= 1
                    length -= 1
                if right < n:
                    trace += ')'
                    right += 1
                    length += 1
                    backtrace(trace)
                    trace = trace[:-1]
                    right -= 1
                    length -= 1

        backtrace('')
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.generateParenthesis(n=3)
    print(ret)
