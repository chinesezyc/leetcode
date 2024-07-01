from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i0, dp_i1 = 0, -prices[0]
        for i in range(1, n):
            # 今天不持股
            dp_i0 = max(dp_i0, dp_i1 + prices[i])
            dp_i1 = max(dp_i1, -prices[i])
        return dp_i0


if __name__ == "__main__":
    #      [5, 6, 7, 1, 2, 3, 4]
    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    ret = solution.maxProfit(prices)
    print(ret)
