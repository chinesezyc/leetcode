from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ret = 0
        while points:
            right = points[0][1]
            ret += 1
            del points[0]
            for i in range(len(points) - 1, -1, -1):
                if points[i][0] <= right <= points[i][1]:
                    del points[i]
        return ret


if __name__ == "__main__":
    solution = Solution()
    result = solution.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
    print(result)
