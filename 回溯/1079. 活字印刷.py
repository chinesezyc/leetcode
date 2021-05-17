from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        length = len(tiles)
        tiles_list = sorted(tiles)
        res = 0

        def backtrace(used: List[bool], num: int):
            nonlocal length, res
            if num > length:
                return

            for i in range(length):
                if used[i]:
                    continue
                if i - 1 >= 0 and tiles_list[i] == tiles_list[i - 1] and used[i - 1] is False:
                    continue
                used[i] = True
                res += 1
                backtrace(used, num + 1)
                used[i] = False

        backtrace([False] * length, 1)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numTilePossibilities(tiles="AAB")
    print(ret)
