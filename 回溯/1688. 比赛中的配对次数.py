from typing import List


class Solution:
    def numberOfMatches(self, n: int) -> int:
        num = 0
        while n > 1:
            if n % 2 == 0:
                n = n / 2
                num += n
            else:
                n = (n - 1) / 2 + 1
                num += n - 1
        return int(num)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numberOfMatches(n=7)
    print(ret)
