from typing import List


class Solution:
    def maxSubArray_dp(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [min(nums)] * (length + 1)
        for i in range(1, length + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
        return max(dp)

    def maxSubArray_dac(self, nums: List[int]) -> int:
        def combine(l: List[int], r: List[int]):
            # 区间内的和
            isum = l[0] + r[0]
            # 区间内从左端点开始的最大子序列
            lsum = max(l[1], l[0] + r[1])
            # 区间内从右端点开始的最大子序列
            rsum = max(r[2], l[2] + r[0])
            # 区间内的最大子序列
            msum = max(l[3], r[3], l[2] + r[1])
            return [isum, lsum, rsum, msum]

        def dac(left: int, right: int):
            if left == right:
                # 下标0：区间内的和
                # 下标1：区间内从左端点开始的最大子序列
                # 下标2：区间内从右端点开始的最大子序列
                # 下标3：区间内的最大子序列
                return [nums[left]] * 4
            mid = (left + right) >> 1
            left_ret = dac(left, mid)
            right_ret = dac(mid + 1, right)
            return combine(left_ret, right_ret)

        return dac(0, len(nums) - 1)[3]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(ret)
