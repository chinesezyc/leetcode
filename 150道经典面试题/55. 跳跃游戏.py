from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        for i in range(len(nums)):
            if pos < i:
                return False
            pos = max(nums[i] + i, pos)
        return pos >= len(nums) - 1


if __name__ == "__main__":
    #      [5, 6, 7, 1, 2, 3, 4]
    nums = [1, 2, 3, 4, 5, 6, 7]

    solution = Solution()
    ret = solution.canJump(nums=nums)
    print(ret)
