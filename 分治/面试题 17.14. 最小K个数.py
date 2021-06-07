from typing import List
import random


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if k >= len(arr):
            return arr

        def findTopKth(low, high):
            pivot = random.randint(low, high)
            arr[low], arr[pivot] = arr[pivot], arr[low]
            base = arr[low]
            i = low
            j = low + 1
            while j <= high:
                if arr[j] < base:
                    arr[i + 1], arr[j] = arr[j], arr[i + 1]
                    i += 1
                j += 1
            arr[low], arr[i] = arr[i], arr[low]
            if i == k - 1:
                return arr[i]
            elif i > k - 1:
                return findTopKth(low, i - 1)
            else:
                return findTopKth(i + 1, high)

        return arr[:findTopKth(0, len(arr) - 1)]


if __name__ == "__main__":
    solution = Solution()
    ret = solution.smallestK(arr=[1, 3, 5, ], k=20)
    print(ret)
