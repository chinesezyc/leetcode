from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        i, high = 1, len(flowerbed)

        while i <= high - 2 and n > 0:
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
            i += 1
        return n == 0


if __name__ == "__main__":
    solution = Solution()
    ret = solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    print(ret)
