from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = [i for i in range(len(s) + 1)]
        result = []
        for c in s:
            if c == 'I':
                result.append(nums.pop(0))
            else:
                result.append(nums.pop(-1))
        result.append(nums.pop(-1))
        return result


if __name__ == "__main__":
    solution = Solution()
    ret = solution.diStringMatch("IDID")
    print(ret)
