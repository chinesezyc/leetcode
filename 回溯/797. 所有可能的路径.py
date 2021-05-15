from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        length = len(s)

        def backtrace(pre_num: int, start: int, nums: int):
            nonlocal length
            if start >= length and nums > 1:
                return True

            for i in range(start, length):
                val_int = int(s[start:i + 1])
                if pre_num - val_int != 1 and nums:
                    continue
                if backtrace(val_int, i + 1, nums + 1):
                    return True
            return False

        return backtrace(-2, 0, 0)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.splitString(s="141312000011")
    print(ret)
