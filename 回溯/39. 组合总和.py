from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        idx = 0

        def backtrace(trace: List[int]):
            nonlocal idx
            tmp = sum(trace)
            if tmp == target:
                tmp_list = sorted(trace).copy()
                if tmp_list not in res:
                    res.append(tmp_list)
                return
            elif tmp > target:
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    continue
                trace.append(candidates[i])
                backtrace(trace)
                trace.pop(-1)

        backtrace([])
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrace(index: int, target_: int, trace: List[int]):
            if target_ == 0:
                res.append(trace.copy())
                return
            elif target < 0:
                return

            for i in range(index, len(candidates)):
                if candidates[i] > target_:
                    continue
                trace.append(candidates[i])
                backtrace(i, target_ - candidates[i], trace)
                trace.pop(-1)

        backtrace(0, target, [])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.combinationSum(candidates=[2, 3, 5], target=8)
    print(ret)
