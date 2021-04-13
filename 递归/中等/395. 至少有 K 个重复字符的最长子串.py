class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(i, k) for i in s.split(c))
        return len(s)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.longestSubstring(s = "ababbc", k = 2)
    print(ret)