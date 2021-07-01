from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [float('inf')] * length
        dp[0] = 0
        for i in range(0, length):
            for j in range(1, nums[i] + 1):
                if i + j < length:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[length - 1]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.jump([1, 5, 1, 3, 6])
    print(ret)
