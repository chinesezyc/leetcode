from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        ret = 0
        while low < high:
            if height[low] > height[high]:
                ret = max(ret, (high - low) * height[high])
                high -= 1
            else:
                ret = max(ret, (high - low) * height[low])
                low += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    ret = solution.maxArea(height=[1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6])
    print(ret)
