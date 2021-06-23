from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        num = 0
        for box in boxTypes:
            if truckSize >= box[0]:
                num += box[0] * box[1]
                truckSize -= box[0]
            else:
                num += truckSize * box[1]
                return num
        return num


if __name__ == "__main__":
    solution = Solution()
    ret = solution.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4)
    print(ret)
