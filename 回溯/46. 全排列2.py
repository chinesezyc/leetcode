from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(trace: List[int],start:int,end:int):
            # print(start,end)
            if len(nums) == len(trace):
                if trace not in res:
                    res.append(trace.copy())
            for each in nums[start:end+1]:
                trace.append(each)
                backtrace(trace,start+1,end)
                trace.pop(-1)

        backtrace([],0,len(nums))
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.permuteUnique(nums=[1, 1, 2])
    print(ret)
