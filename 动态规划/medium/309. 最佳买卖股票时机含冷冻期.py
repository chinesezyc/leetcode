from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(prices.__len__())]
        dp[0][1] = -prices[0]
        for i in range(1, prices.__len__()):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[-1][0]


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxProfit([1, 2, 3, 0, 2])
    print(result)
