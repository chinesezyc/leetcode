import collections
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def cal(s):
            res = 0
            for t in s:
                res = res * 10 + t
            return res

        Q = collections.deque()
        for i in range(1, 10):
            Q.append([i])
        res = []
        while Q:
            v = Q.popleft()
            if len(v) == n:
                res.append(cal(v))
            elif k == 0:
                v.append(v[-1])
                Q.append(v)
            else:
                if v[-1] - k >= 0:
                    t = v.copy()
                    t.append(t[-1] - k)
                    Q.append(t)
                if v[-1] + k < 10:
                    t = v.copy()
                    t.append(t[-1] + k)
                    Q.append(t)
        return res



if __name__ == "__main__":
    solution = Solution()
    ret = solution.numsSameConsecDiff(n=3, k=7)
    print(ret)
