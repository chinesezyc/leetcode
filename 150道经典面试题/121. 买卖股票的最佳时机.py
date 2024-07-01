from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in prices]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, n):
            # 今天不持股
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return dp[n - 1][0]


if __name__ == "__main__":
    #      [5, 6, 7, 1, 2, 3, 4]
    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    ret = solution.maxProfit(prices)
    print(ret)
