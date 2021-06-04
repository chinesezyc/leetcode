import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x:x[0]**2+x[1]**2)
        return points[:k]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.kClosest(points=[[1, 3], [-2, 2]], k=1)
    print(ret)
