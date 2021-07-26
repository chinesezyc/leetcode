from typing import List


class Solution:
    def maxProfit_dp(self, prices: List[int]) -> int:
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, prices.__len__()):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

    def maxProfit(self, prices: List[int]) -> int:
        prices.append(-1)
        stack = []
        max_val = 0
        for i in range(prices.__len__()):
            while stack and prices[i] < stack[-1]:
                max_val = max(max_val, stack[-1] - stack[0])
                stack.pop()
            stack.append(prices[i])

        return max_val


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(result)
