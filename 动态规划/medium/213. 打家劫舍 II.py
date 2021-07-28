from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums.__len__() <= 2:
            return max(nums)

        for k in range(nums.__len__()):
            dp = [0] * nums.__len__()
            k = k % nums.__len__()
            dp[k + 0], dp[k + 1] = nums[k+0], max(nums[k:k+2])
            for i in range(k + 2, k+nums.__len__()):
                i = i % nums.__len__()

                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.rob([3, 2, 6, 5, 0, 3])
    print(result)
