from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        ret = 1
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret


if __name__ == "__main__":
    solution = Solution()
    ret = solution.lengthOfLIS(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(ret)
