from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_pirce = prices[0]
        for p in prices[1:]:
            min_pirce = min(min_pirce, p)
            ans = max(ans, p - min_pirce)

        return ans


if __name__ == "__main__":
    #      [5, 6, 7, 1, 2, 3, 4]
    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    ret = solution.maxProfit(prices)
    print(ret)
