from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            if stones[0] != stones[1]:
                stones.append(abs(stones[0] - stones[1]))
            del stones[0], stones[0]
        return stones[0] if len(stones) else 0


if __name__ == "__main__":
    solution = Solution()
    ret = solution.lastStoneWeight([2, 7, 4, 1, 8, 1])
    print(ret)
