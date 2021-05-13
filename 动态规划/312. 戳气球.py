from typing import List
import numpy as np


class Solution:
    def maxCoins1(self, nums: List[int]) -> int:
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

        return int(backtrace(0, length - 1))

    def maxCoins(self, nums: List[int]) -> int:
        coins = [1] + nums + [1]
        length = len(coins)
        dp = [[0] * length for _ in range(length)]

        for i in range(length - 3, -1, -1):
            for j in range(i + 2, length):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + coins[i] * coins[k] * coins[j])
        return int(dp[0][length - 1])


if __name__ == "__main__":
    solution = Solution()
    ret = solution.maxCoins(nums= [3]*5)
    print(ret)
    length=5000
    import time
    a=time.process_time()
    dp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            dp[i][j] = max(dp[i][j],1)
    b=time.process_time()
    m=b*1000-a*1000
    print(b*1000-a*1000)

    a=time.process_time()
    dp = np.zeros(shape=(length, length), dtype=int)
    for i in range(length):
        for j in range(length):
            dp[i][j] = max(dp[i][j],1)

    b=time.process_time()
    n=b*1000-a*1000
    print(b*1000-a*1000)

    print(n/m)