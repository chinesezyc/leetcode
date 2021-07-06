import collections
from typing import List


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remain_counts = collections.Counter(s)
        stack = []
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and remain_counts[stack[-1]]:
                    stack.pop()
                stack.append(c)
            remain_counts[c] -= 1
        return ''.join(stack)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.removeDuplicateLetters(s="cbacdcbc")
    print(ret)
