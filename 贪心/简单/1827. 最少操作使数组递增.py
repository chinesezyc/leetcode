from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pre = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= pre:
                cnt += pre - nums[i] + 1
                nums[i] = pre + 1
            pre = nums[i]

        return cnt


if __name__ == "__main__":
    solution = Solution()
    ret = solution.minOperations(nums=[1, 1, 1])
    print(ret)
