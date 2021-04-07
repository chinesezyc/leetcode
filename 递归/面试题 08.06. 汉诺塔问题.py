from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)

        def move(n: int, A: List[int], B: List[int], C: List[int]):
            if n == 1:
                C.append(A.pop(-1))
            else:
                move(n - 1, A, C, B)
                C.append(A.pop(-1))
                move(n - 1, B, A, C)

        move(n, A, B, C)
        return C



if __name__ == "__main__":
    solution = Solution()
    ret = solution.hanota(A = [2, 1, 0], B = [], C = [])
    print(ret)