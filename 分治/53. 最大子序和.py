from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [min(nums)] * (length + 1)
        for i in range(1, length + 1):
            dp[i] = max(nums[i-1], dp[i - 1] + nums[i - 1])
        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.maxSubArray(nums=[-1])
    print(ret)
