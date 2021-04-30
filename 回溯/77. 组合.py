from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrace(idx: int, trace: List[int], length: int):
            if length == k:
                res.append(trace.copy())
                return
            for i in range(idx, n + 1):
                trace.append(i)
                length += 1
                backtrace(i + 1, trace, length)
                trace.pop(-1)
                length -= 1

        backtrace(1, [], 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.combine(n=4, k=2)
    print(ret)
