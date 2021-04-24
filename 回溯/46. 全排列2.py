from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(trace: List[int], tmp_nums: List[int]):
            if len(tmp_nums) == 0:
                if trace not in res:
                    res.append(trace.copy())
            for idx in range(len(tmp_nums)):
                each = tmp_nums.pop(idx)
                trace.append(each)
                backtrace(trace, tmp_nums)
                trace.pop(-1)
                tmp_nums.insert(idx, each)

        backtrace([], nums)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.permuteUnique(nums=[1, 1, 2])
    print(ret)
