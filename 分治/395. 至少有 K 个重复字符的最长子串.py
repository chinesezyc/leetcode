from typing import List


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        char_nums = {}
        for c in s:
            if char_nums.__contains__(c):
                char_nums[c] += 1
            else:
                char_nums[c] = 1

        for c in char_nums:
            if char_nums[c] < k:
                return max(self.longestSubstring(i, k) for i in s.split(c))
        return len(s)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.longestSubstring(s="aaabb", k=3)
    print(ret)
