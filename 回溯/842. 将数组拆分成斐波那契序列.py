from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        length = len(num)
        F = 2 ** 31 - 1
        res = []

        def backtrace(start: int, nums: int):
            nonlocal length, res, F
            if start >= length:
                return nums > 2
            val_int = 0
            for i in range(start, length):
                if i > start and num[start] == '0':
                    break
                val_int = val_int * 10 + ord(num[i]) - ord("0")
                if val_int > F:
                    break
                if nums < 2:
                    res.append(val_int)
                    if backtrace(i + 1, nums + 1):
                        return True
                    res.pop(-1)
                elif nums >= 2 and res[-2] + res[-1] == val_int:
                    res.append(val_int)

                    if backtrace(i + 1, nums + 1):
                        return True
                    res.pop(-1)
            return False

        backtrace(0, 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.splitIntoFibonacci(num="123456579")
    print(ret)