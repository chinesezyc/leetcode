import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = {}
        for i, [x, y] in enumerate(points):
            dist[i] = (x ** 2 + y ** 2)
        l = sorted(dist.items(), key=lambda x1: x1[1], reverse=False)
        return [points[i[0]] for i in l[:k]]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.kClosest(points=[[1, 3], [-2, 2]], k=1)
    print(ret)
