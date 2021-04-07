from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]

        return [shorter * k + i * (longer - shorter) for i in range(0, k + 1)]




if __name__ == "__main__":
    solution = Solution()
    ret = solution.divingBoard(1, 2, 3)
    print(ret)