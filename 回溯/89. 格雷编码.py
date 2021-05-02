from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []

        def backtrace(trace: str):
            pass

        backtrace('')
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.grayCode(n=4)
    print(ret)
