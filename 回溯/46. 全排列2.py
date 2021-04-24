from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrace(trace: List[int], tmp_nums: List[int], pre_choice: int = None):
            if len(tmp_nums) == 0:
                res.append(trace.copy())
            for idx in range(len(tmp_nums)):
                if pre_choice == tmp_nums[idx]:
                    continue
                pre_choice = tmp_nums[idx]
                each = tmp_nums.pop(idx)
                trace.append(each)
                backtrace(trace, tmp_nums)
                trace.pop(-1)
                tmp_nums.insert(idx, each)

        backtrace([], nums)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.permuteUnique(nums=[3, 3, 0, 3])
    print(ret)
