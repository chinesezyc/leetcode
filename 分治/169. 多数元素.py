from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        res = {}
        for val in nums:
            if res.__contains__(val):
                res[val] += 1
            else:
                res[val] = 0
        return max(res.items(), key=lambda x: x[1])[0]

    def majorityElement2(self, nums: List[int]) -> int:
        def dac(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) >> 1
            left_num = dac(left, mid)
            right_num = dac(mid + 1, right)
            if left_num == right_num:
                return left_num
            else:
                left_count = sum([1 for i in range(left, mid + 1) if nums[i] == left_num])
                right_count = sum([1 for i in range(mid + 1, right + 1) if nums[i] == right_num])
                return left_num if left_count > right_count else right_num

        return dac(0, len(nums) - 1)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.majorityElement([2, 2, 1, 1, 1, 1, 2])
    print(ret)
