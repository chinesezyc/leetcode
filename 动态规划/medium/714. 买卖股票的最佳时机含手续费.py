from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in range(prices.__len__())]
        dp[0][1] = -prices[0]-fee
        for i in range(1, prices.__len__()):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]-fee)

        return dp[-1][0]


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)
    print(result)
