from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        res = []

        def backtrace(trace: List[int], idx: int, use_bool: List[bool]):
            if n == idx:
                res.append(trace.copy())
                return
            for i in range(1, n + 1):
                if idx == 1 and i == 0 and n > 1:
                    continue
                if use_bool[i]:
                    continue
                if i % (len(trace) + 1) == 0 or (len(trace) + 1) % i == 0:
                    use_bool[i] = True
                    trace.append(i)
                    backtrace(trace, idx + 1, use_bool)
                    use_bool[i] = False
                    trace.pop(-1)

        backtrace([], 0, [False] * (n+1))
        return len(res)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countArrangement(n=10)
    print(ret)
