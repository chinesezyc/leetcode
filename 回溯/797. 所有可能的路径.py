from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def backtrace(point: int, trace: List[int]):
            nonlocal res
            if point == len(graph) - 1:
                res.append(trace.copy())
                return

            for i in graph[point]:
                trace.append(i)
                backtrace(i, trace)
                trace.pop(-1)

        for p in graph[0]:
            backtrace(p, [0, p])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.allPathsSourceTarget(graph=[[4,3,1],[3,2,4],[3],[4],[]])
    print(ret)
