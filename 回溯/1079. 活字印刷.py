from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        length = len(tiles)
        res = []
        tiles_list = sorted(tiles)

        def backtrace(trace: str, used: List[bool]):
            nonlocal length, res
            if trace not in res and trace != '':
                res.append(trace)
            for i in range(length):
                if used[i]:
                    continue
                trace += tiles_list[i]
                used[i] = True
                backtrace(trace, used)
                trace = trace[:-1]
                used[i] = False

        backtrace('', [False] * length)
        return len(res)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.numTilePossibilities(tiles="AAB")
    print(ret)
