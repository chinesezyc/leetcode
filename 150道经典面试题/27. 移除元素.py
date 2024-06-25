from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    m = 2

    solution = Solution()
    solution.removeElement(nums=nums, val=m)
    print(nums)
