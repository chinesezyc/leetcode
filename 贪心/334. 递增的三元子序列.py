from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low, mid = float('inf'), float('inf')
        for c in nums:
            if c <= low:
                low = c
            elif c <= mid:
                mid = c
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    ret = solution.increasingTriplet(nums=[2, 1, 5, 0, 4, 6])
    print(ret)
