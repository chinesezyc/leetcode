from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for _ in range(k):
            nums[0] = -nums[0]
            nums.sort()
        return sum(nums)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.largestSumAfterKNegations(nums=[4, 2, 3], k=1)
    print(ret)
