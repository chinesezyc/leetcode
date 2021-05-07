from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrace(choice: List[str], start_idx: int):
            if len(s) == start_idx + 1:
                res.append(choice.copy())
                return
            for i in range(start_idx, len(s) + 1):

                if s[start_idx:i + 1] != s[start_idx:i + 1][::-1]:
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
