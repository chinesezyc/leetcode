from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrace(trace: str):
            pass

        backtrace('')
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.restoreIpAddresses(s="25525511135")
    print(ret)
