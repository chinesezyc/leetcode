from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        k, i, high = 0, 1, len(flowerbed)

        while i <= high or k > 0:
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                k -= 1
                flowerbed[i] = 1
                i += 1
            else:
                i += 1
        return k == 0


if __name__ == "__main__":
    solution = Solution()
    ret = solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    print(ret)
