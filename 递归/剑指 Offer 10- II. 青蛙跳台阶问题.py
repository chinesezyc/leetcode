class Solution:
    def numWays1(self, n: int) -> int:
        def fab(n: int) -> int:
            if n == 0:
                return 1
            if n <= 2:
                return n
            return fab(n - 1) + fab(n - 2)

        return fab(n)

    def numWays2(self, n: int) -> int:
        helper = dict()

        def fab(n: int) -> int:
            if helper.__contains__(n):
                return helper[n]
            if n <= 1:
                helper[n] = n
                return helper[n]
            helper[n] = fab(n - 1) + fab(n - 2)
            return helper[n]

        return fab(n) % 1000000007

    def numWays(self, n: int) -> int:
        i, j = 1, 1
        for _ in range(n - 1):
            i, j = j, i + j
        return j % 1000000007


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numWays(7)
    print(ret)
