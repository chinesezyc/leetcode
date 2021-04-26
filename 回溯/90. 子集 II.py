from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrace(idx: int, trace: List[int]):
            pre_num = None
            res.append(trace.copy())
            for i in range(idx, len(nums)):
                if pre_num == nums[i]:
                    continue
                pre_num = nums[i]
                trace.append(nums[i])
                backtrace(i + 1, trace)
                trace.pop(-1)

        backtrace(0, [])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.subsetsWithDup(nums=[1, 2, 2])
    print(ret)
