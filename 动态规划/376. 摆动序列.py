from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1
        return 0 if 0 == len(nums) else max(up, down)


if __name__ == "__main__":
    solution = Solution()
    result = solution.wiggleMaxLength(nums=[1, 7, 4, 9, 2, 5])
    print(result)
