from typing import List


class Solution:
    def numberOfMatches1(self, n: int) -> int:
        num = 0
        while n > 1:
            if n % 2 == 0:
                n = n / 2
                num += n
            else:
                n = (n - 1) / 2 + 1
                num += n - 1
        return int(num)

    def numberOfMatches(self, n: int) -> int:
        if n <= 1:
            return 0
        return n // 2 + self.numberOfMatches(n // 2 + 1 if n % 2 else n // 2)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numberOfMatches(n=7)
    print(ret)
