from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0

        def backtrace(trace: int, use_bool: List[bool]):
            nonlocal res
            if trace > n:
                res += 1
                # return
            for i in range(1, n + 1):
                if use_bool[i]:
                    continue
                if i % trace == 0 or trace % i == 0:
                    use_bool[i] = True
                    backtrace(trace + 1, use_bool)
                    use_bool[i] = False

        backtrace(1, [False] * (n + 1))
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countArrangement(n=10)
    print(ret)
