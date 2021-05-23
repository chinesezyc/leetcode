from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        count = 0
        for each in nums:
            if count == 0:
                num = each
            count = count + 1 if each == num else count - 1
        return num


if __name__ == "__main__":
    solution = Solution()
    ret = solution.majorityElement(nums=[1, 2, 3, 2, 2, 2, 5, 4, 2])
    print(ret)
