from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    print(ret)
