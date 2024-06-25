from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        pre_val = float("inf")
        for cur_val in nums:
            if cur_val != pre_val:
                nums[p], pre_val =cur_val,cur_val
                p += 1
        return p


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    solution.removeDuplicates(nums=nums)
    print(nums)
