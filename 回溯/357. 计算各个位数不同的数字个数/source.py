from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        res = []

        def backtrace(trace:str):
            if n == len(trace):
                res.append(int(trace))

            for each in nums:
                if each in trace:
                    continue
                trace.append(each)
                backtrace(trace)
                trace.pop(-1)

        backtrace([])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.permute(nums=[1, 2, 3])
    print(ret)
