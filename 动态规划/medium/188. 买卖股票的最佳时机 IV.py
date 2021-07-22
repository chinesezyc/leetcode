from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices.__len__() < 2:
            return 0
        K = min(k, prices.__len__() // 2) + 1
        dp = [[[0] * K, [0] * K] for _ in range(prices.__len__())]
        for i in range(K):
            dp[0][1][i] = -prices[0]

        for i in range(1, prices.__len__()):
            for j in range(1, K):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j] + prices[i])
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j - 1] - prices[i])

        return dp[-1][0][-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3])
    print(result)
