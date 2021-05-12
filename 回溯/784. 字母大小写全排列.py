from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        length = len(s)

        def backtrace(trace: str, start_idx: int):
            nonlocal res, length
            if start_idx == length:
                res.append(trace)
                return
            for i in range(start_idx, length):
                if s[i].isascii():
                    trace += s[i]
                    backtrace(trace, i + 1)
                    trace = trace[:-1]
                else:
                    for c in [s[i].lower(), s[i].upper()]:
                        trace += c
                        backtrace(trace, i + 1)
                        trace = trace[:-1]

        backtrace('', 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.letterCasePermutation(s="a1b2")
    print(ret)
