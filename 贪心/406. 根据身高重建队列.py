from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])
        ret = []
        for i in people:
            ret.insert(i[1], i)
        return ret


if __name__ == "__main__":
    solution = Solution()
    result = solution.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    print(result)
