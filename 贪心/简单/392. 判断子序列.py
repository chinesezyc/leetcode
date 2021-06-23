from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n, i, j = len(s), len(t), 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i >= m


if __name__ == "__main__":
    solution = Solution()
    ret = solution.isSubsequence(s="abc", t="ahbgdc")
    print(ret)
