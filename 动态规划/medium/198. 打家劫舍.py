from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums.__len__() <= 2:
            return max(nums)
        dp = [0] * nums.__len__()
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, nums.__len__()):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.rob([3, 2, 6, 5, 0, 3])
    print(result)
