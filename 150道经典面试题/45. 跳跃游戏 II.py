import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


if __name__ == "__main__":
    #      [5, 6, 7, 1, 2, 3, 4]
    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    ret = solution.jump(prices)
    print(ret)
