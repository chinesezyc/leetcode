from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ret = 1
        right = points[0][1]

        for p in points:
            if p[0] > right:
                right = p[1]
                ret += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    result = solution.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
    print(result)
