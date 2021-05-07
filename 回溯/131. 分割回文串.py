from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def check(trace: str) -> bool:
            i, j = 0, len(trace) - 1
            while i < j:
                if trace[i] != trace[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrace(choice: List[str], start_idx: int):
            if len(s) == start_idx:
                res.append(choice.copy())
                return
            for i in range(start_idx, len(s) + 1):

                if not check(s[start_idx:i + 1]):
                    continue

                choice.append(s[start_idx:i + 1])
                backtrace(choice, i + 1)
                choice.pop(-1)

        backtrace([], 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.partition(s="aab")
    print(ret)
