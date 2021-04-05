class Solution:
    def tribonacci1(self, n: int) -> int:
        def fab(n: int) -> int:
            if n == 0:
                return 0
            if n <= 2:
                return 1
            return fab(n - 1) + fab(n - 2) + fab(n - 3)

        return fab(n)

    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        i, j, k = 0, 1, 1
        for _ in range(3, n + 1):
            i, j, k = j, k, i + j + k
        return k

    def tribonacci(self, n: int) -> int:
        helper = dict()

        def fab(n: int) -> int:
            if helper.__contains__(n):
                return helper[n]
            if n == 0:
                helper[0] = 0
                return 0
            if n <= 2:
                helper[n] = 1
                return 1
            helper[n] = fab(n - 1) + fab(n - 2) + fab(n - 3)
            return helper[n]

        return fab(n)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.tribonacci(25)
    print(ret)
