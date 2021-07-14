from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        people.sort(key=lambda x: [-x[0], x[1]])
        ret = []
        for i in people:
            ret.insert(i[1], i)
        return ret


if __name__ == "__main__":
    solution = Solution()
    result = solution.wiggleMaxLength(nums = [1,7,4,9,2,5])
    print(result)
