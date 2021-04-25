from typing import List


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = []
        t = []

        def backtrace(idx: int, n: int):
            if idx == n:
                res.append(t.copy())
                return
            t.append(nums[idx])
            backtrace(idx + 1, len(nums))
            t.pop(-1)
            backtrace(idx + 1, len(nums))

        backtrace(0, len(nums))
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(idx: int, tmp_nums: List[int]):
            res.append(tmp_nums.copy())
            for i in range(idx, len(nums)):
                backtrace(i + 1, tmp_nums + [nums[i]])

        backtrace(0, [])
        return res

if __name__ == "__main__":
    solution = Solution()
    ret = solution.subsets(nums=[1, 2, 3])
    print(ret)
