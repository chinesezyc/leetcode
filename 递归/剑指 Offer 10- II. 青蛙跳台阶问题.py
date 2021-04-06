class Solution:
    def numWays(self, n: int) -> int:
        def fab(n: int) -> int:
            if n == 0:
                return 1
            if n <= 2:
                return n
            return fab(n - 1) + fab(n - 2)

        return fab(n)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numWays(7)
    print(ret)
