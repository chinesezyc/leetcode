from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums.__len__() <= 2:
            return max(nums)

        def fun(sub_nums: List[int]) -> int:
            if sub_nums.__len__() <= 2:
                return max(sub_nums)
            dp = [0] * sub_nums.__len__()
            dp[0], dp[1] = sub_nums[0], max(sub_nums[:2])
            for i in range(2, sub_nums.__len__()):
                dp[i] = max(dp[i - 1], dp[i - 2] + sub_nums[i])
            return dp[-1]

        return max(fun(nums[:-1]), fun(nums[1:]))


if __name__ == "__main__":
    solution = Solution()
    result = solution.rob([3,4,3])
    print(result)
