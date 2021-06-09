from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start, end = 0, len(s)
        for c in t:
            if start >= end:
                return True
            if c == s[start]:
                start += 1
        return start >= end


if __name__ == "__main__":
    solution = Solution()
    ret = solution.isSubsequence(s="abc", t="ahbgdc")
    print(ret)
