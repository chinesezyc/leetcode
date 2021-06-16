from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if strs is None:
            return 0
        width, height = len(strs[0]), len(strs)
        ret = 0
        for w in range(width):
            for h in range(1, height):
                if strs[h][w] < strs[h - 1][w]:
                    ret += 1
                    break
        return ret


if __name__ == "__main__":
    solution = Solution()
    ret = solution.minDeletionSize(strs=["cba", "daf", "ghi"])
    print(ret)
