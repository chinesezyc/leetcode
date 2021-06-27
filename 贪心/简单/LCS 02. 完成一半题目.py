from typing import List
import collections


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        n = len(questions) // 2
        num_freq = collections.Counter(questions)
        xf = sorted(num_freq.items(), key=lambda x: -x[1])

        kind = 0
        cnt = 0
        for x, f in xf:
            if cnt >= n:
                return kind
            else:
                cnt += f
                kind += 1
        return kind


if __name__ == "__main__":
    solution = Solution()
    ret = solution.halfQuestions(questions=[1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6])
    print(ret)
