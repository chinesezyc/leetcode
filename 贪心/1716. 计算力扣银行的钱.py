from typing import List


class Solution:
    def totalMoney(self, n: int) -> int:
        m, k = n // 7, n % 7
        return int((7 * m ** 2 + k ** 2 + 2 * m * k + 49 * m + k) / 2)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.totalMoney(n=20)
    print(ret)
