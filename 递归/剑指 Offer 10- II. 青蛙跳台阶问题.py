class Solution:
    def numWays1(self, n: int) -> int:
        def fab(n: int) -> int:
            if n == 0:
                return 1
            if n <= 2:
                return n
            return fab(n - 1) + fab(n - 2)

        return fab(n)

    def numWays(self, n: int) -> int:
        helper = dict()

        def fab(n: int) -> int:
            if helper.__contains__(n):
                return helper[n]
            if n == 0:
                helper[n] = 1
                return helper[n]
            if n <= 2:
                helper[n] = n
                return helper[n]
            helper[n] = fab(n - 1) + fab(n - 2)
            return helper[n]

        return fab(n)%1000000007

if __name__ == "__main__":
    solution = Solution()
    ret = solution.numWays(7)
    print(ret)
