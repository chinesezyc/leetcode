from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        pre_val = nums[0]
        flag = False
        for i in range(1, len(nums)):
            if nums[i] != pre_val:
                nums[p] = nums[i]
                p += 1
                pre_val = nums[i]
                flag = False
            else:
                if flag is False:
                    nums[p] = pre_val
                    p += 1
                    pre_val = nums[i]
                    flag = True

        return p


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    solution.removeDuplicates(nums=nums)
    print(nums)
