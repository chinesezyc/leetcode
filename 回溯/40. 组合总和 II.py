from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrace(index: int, target_: int, trace: List[int]):
            pre_num = None
            if target_ == 0:
                res.append(trace.copy())
                return
            elif target < 0:
                return

            for i in range(index, len(candidates)):
                if target_ - candidates[i] < 0:
                    continue
                if pre_num == candidates[i]:
                    continue
                pre_num = candidates[i]
                trace.append(candidates[i])
                backtrace(i + 1, target_ - candidates[i], trace)
                trace.pop(-1)

        backtrace(0, target, [])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    print(ret)
