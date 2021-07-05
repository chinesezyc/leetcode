import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x: str, y: str):
            return int(y + x) - int(x + y)

        nums = sorted(map(str, nums), key=functools.cmp_to_key(cmp))
        return '0' if nums[0] == '0' else ''.join(nums)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.largestNumber(nums=[3, 30, 34, 5, 9])
    print(ret)
