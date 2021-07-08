from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.findLengthOfLCIS(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(ret)
