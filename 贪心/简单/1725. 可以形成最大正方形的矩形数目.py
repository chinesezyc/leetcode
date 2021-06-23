from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides = []
        max_len = -1
        for rect in rectangles:
            val = min(rect)
            sides.append(val)
            max_len = max(max_len, val)
        return sides.count(max_len)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countGoodRectangles(rectangles=[[6, 8], [3, 9], [5, 12], [16, 5]])
    print(ret)
