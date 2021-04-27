from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrace(idx: int, trace: List[int]):
            tmp = sum(trace)
            if tmp == target:
                res.append(trace.copy())
                return
            elif tmp > target:
                return

            for i in range(idx, len(candidates)):
                if candidates[i]>target:
                    continue
                trace.append(candidates[i])
                backtrace(i + 1, trace)
                trace.pop(-1)
                # backtrace(i + 1, trace)


        backtrace(0, [])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.combinationSum(candidates=[2, 3, 6, 7], target=7)
    print(ret)
