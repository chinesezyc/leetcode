from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        result, total, half_num = [], 0, sum(nums) / 2
        for num in nums:
            total += num
            result.append(num)
            if total > half_num:
                return result


if __name__ == "__main__":
    solution = Solution()
    ret = solution.minSubsequence(nums=[4, 3, 10, 9, 8])
    print(ret)
