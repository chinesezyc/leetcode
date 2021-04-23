from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtrace(self, nums: List[int], trace: List[int]):
        if len(nums) == len(trace):
            self.res.append(trace.copy())
        for each in nums:
            if each in trace:
                continue
            trace.append(each)
            self.backtrace(nums, trace)
            trace.pop(-1)

    def permute1(self, nums: List[int]) -> List[List[int]]:

        self.backtrace(nums, [])
        return self.res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(nums: List[int], trace: List[int]):
            if len(nums) == len(trace):
                res.append(trace.copy())
            for each in nums:
                if each in trace:
                    continue
                trace.append(each)
                backtrace(nums, trace)
                trace.pop(-1)

        backtrace(nums, [])
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(trace: List[int]):
            if len(nums) == len(trace):
                res.append(trace.copy())
            for each in nums:
                if each in trace:
                    continue
                trace.append(each)
                backtrace(trace)
                trace.pop(-1)

        backtrace([])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.permute(nums=[1, 2, 3])
    print(ret)
