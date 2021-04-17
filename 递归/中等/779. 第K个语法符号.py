class Solution:
    def kthGrammar2(self, N: int, K: int) -> int:
        res = [0]
        for _ in range(1, N):
            length = len(res)
            for i in range(length):
                val = res.pop(0)
                if val == 0:
                    res.append(0)
                    res.append(1)
                else:
                    res.append(1)
                    res.append(0)
        return res[K - 1]

    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        return (1 - K % 2) ^ self.kthGrammar(N - 1, (K + 1) // 2)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.kthGrammar(30, 1)
    print(ret)
