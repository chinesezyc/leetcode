from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def dac(low, high):
            if low >= high:
                return nums[low]
            mid = (low + high) // 2
            l_num = dac(low, mid)
            r_num = dac(mid+1, high)
            if l_num == r_num:
                return l_num
            else:
                l_num_count = sum([1 for val in nums[low:mid+1] if val == l_num])
                r_num_count = sum([1 for val in nums[mid+1:high+1] if val == r_num])
                return l_num if l_num_count > r_num_count else r_num

        return dac(0, len(nums)-1)


if __name__ == "__main__":
    nums =[6,5,5]
    solution = Solution()
    solution.majorityElement(nums=nums)
    print(nums)
