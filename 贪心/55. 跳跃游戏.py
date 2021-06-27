from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [False] * length
        dp[0] = True
        for i in range(1, length):
            for j in range(i - 1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break

        return dp[length - 1]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.canJump(nums=[1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6])
    print(ret)
