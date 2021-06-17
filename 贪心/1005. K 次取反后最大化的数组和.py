from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,length=0,len(nums)
        for _ in range(k):
            if nums[i]==0:
                continue
            elif nums[i]<0:
                nums[i]=-nums[i]
                i+=1
        print(nums)


if __name__ == "__main__":
    solution = Solution()
    ret = solution.largestSumAfterKNegations(nums=[4, 2, 3], k=1)
    print(ret)
