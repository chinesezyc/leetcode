from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides = []
        for rect in rectangles:
            sides.append(min(rect))
        return sides.count(max(sides))


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countGoodRectangles(rectangles=[[6, 8], [3, 9], [5, 12], [16, 5]])
    print(ret)
