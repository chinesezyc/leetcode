import math
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        n = len(nums)
        gcd = math.gcd(n, k)
        for i in range(gcd):
            pos = i
            pre_val = nums[i]
            for _ in range(n//gcd):
                pos = (pos + k) % n
                nums[pos], pre_val = pre_val, nums[pos]


if __name__ == "__main__":
    #      [5, 6, 7, 1, 2, 3, 4]
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    solution = Solution()
    solution.rotate(nums=nums, k=k)
    print(nums)
