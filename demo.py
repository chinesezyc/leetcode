from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        num_list = [True] * n
        num_list[0], num_list[1] = False, False
        for i in range(2, int(pow(n, 0.5)) + 1):
            if num_list[i]:
                num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)

        return sum(num_list)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countPrimes(4)
    print(ret)
