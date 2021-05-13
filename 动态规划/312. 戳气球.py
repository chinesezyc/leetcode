from typing import List
import numpy as np


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [1] + nums + [1]
        length = len(coins)
        cache = np.ones(shape=(length, length), dtype=int) * -1

        def backtrace(left: int, right: int):
            nonlocal coins, cache
            if left == right - 1:
                return 0
            if cache[left][right] != -1:
                return cache[left][right]
            for i in range(left + 1, right):
                cache[left][right] = max(cache[left][right],
                                         backtrace(left, i) + backtrace(i, right) + coins[left] * coins[i] * coins[
                                             right])
            return cache[left][right]

        return int(backtrace(0, length - 1)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.maxCoins(nums=[3, 1, 5, 8])
    print(ret)
