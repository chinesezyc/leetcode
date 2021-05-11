from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0

        def backtrace(trace: int, idx: int, use_bool: List[bool]):
            nonlocal res
            if n == idx:
                res += 1
                return
            for i in range(1, n + 1):
                if idx == 1 and i == 0 and n > 1:
                    continue
                if use_bool[i]:
                    continue
                if i % trace == 0 or trace % i == 0:
                    use_bool[i] = True
                    trace += 1
                    backtrace(trace, idx + 1, use_bool)
                    use_bool[i] = False
                    trace -= 1

        backtrace(1, 0, [False] * (n + 1))
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countArrangement(n=10)
    print(ret)
