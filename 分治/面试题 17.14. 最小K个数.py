from typing import List
import random


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.smallestK(arr=[11, 3, 5, ], k=1)
    print(ret)
