from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def fetchCurValue(l, r):
            if l < r and num[l] == '0':
                return -1
            res = 0
            while l <= r:
                res = res * 10 + int(num[l])
                l += 1
            return res

        def backtrace(start_idx: int, total: int, pre: int, k: int) -> bool:
            if start_idx == len(num):
                return k > 2

            for i in range(start_idx, len(num)):
                cur = fetchCurValue(start_idx, i)
                if cur < 0:
                    break
                if k >= 2 and total != cur:
                    continue

                if backtrace(i + 1, pre + cur, cur, k + 1):
                    return True

            return False

        return backtrace(0, 0, 0, 0)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.isAdditiveNumber(num="199100199")
    print(ret)
