from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        def backtrace(idx: int, use_bool: List[bool]) -> int:
            count = 0
            if n != idx:
                for i in range(0, 10):
                    if idx == 1 and i == 0 and n > 1:
                        continue
                    if use_bool[i]:
                        continue
                    use_bool[i] = True
                    count += backtrace(idx + 1, use_bool) + 1
                    use_bool[i] = False
            return count

        return backtrace(0, [False] * 10)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countNumbersWithUniqueDigits(n=2)
    print(ret)
