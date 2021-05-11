from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 0:
            return 1
        count = 0

        def backtrace(idx: int, use_bool: List[bool]) -> int:
            nonlocal count
            if n != idx:
                for i in range(0, 3):
                    if idx == 1 and i == 0 and n > 1:
                        continue
                    if use_bool[i]:
                        continue
                    use_bool[i] = True
                    backtrace(idx + 1, use_bool)
                    use_bool[i] = False
            else:
                count += 1
            return count

        return backtrace(0, [False] * 10)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.countArrangement(n=2)
    print(ret)
