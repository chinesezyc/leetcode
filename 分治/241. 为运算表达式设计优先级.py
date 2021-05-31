from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, c in enumerate(expression):
            if c in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if c == '-':
                            res.append(l - r)
                        elif c == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.diffWaysToCompute("2-1-1")
    print(ret)
