from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n, i, j = len(g), len(s), 0, 0
        g.sort()
        s.sort()
        ret = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                ret += 1
                i += 1
            j += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    ret = solution.findContentChildren(g=[1, 2, 3], s=[1, 2,3,4])
    print(ret)
