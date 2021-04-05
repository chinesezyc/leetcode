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


if __name__ == "__main__":
    solution = Solution()
    ret = solution.tribonacci(25)
    print(ret)
