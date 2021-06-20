from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L, R = 0, 0
        ret = 0
        for c in s:
            if c == 'R':
                R += 1
            else:
                L += 1
            if L == R:
                ret += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    ret = solution.balancedStringSplit(s="RLRRLLRLRL")
    print(ret)
