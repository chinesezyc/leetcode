from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result, i = 0, len(nums)
        while i > 0:
            result += nums[i - 2]
            i -= 2
        return result


if __name__ == "__main__":
    solution = Solution()
    ret = solution.arrayPairSum([1,2,3,4])
    print(ret)
