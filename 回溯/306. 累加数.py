from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backtrace(start_idx: int, val1: int, val2: int) -> bool:
            if start_idx-1 == len(num):
                return True

            for i in range(start_idx+1, len(num)+1):
                if num[i-1] == '0':
                    break
                if val1 and val2 and val1 + val2 != int(num[start_idx:start_idx + i]):
                    break

                tmp = val1
                val1 = val2
                val2 = int(num[start_idx:i])
                if backtrace(i, val1, val2):
                    return True
                val2 = val1
                val1 = tmp
            return False

        return backtrace(0, None, None)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.isAdditiveNumber(num="112")
    print(ret)
