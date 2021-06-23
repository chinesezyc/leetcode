from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tmp, ret = 0, 0
        for c in s:
            if c == 'R':
                tmp += 1
            else:
                tmp -= 1
            if tmp == 0:
                ret += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    ret = solution.balancedStringSplit(s="RLRRLLRLRL")
    print(ret)
