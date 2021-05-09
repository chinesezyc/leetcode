from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrace(start_idx: int, total_num: int, num_len: int, choice: List[int]):
            if total_num == n and num_len == k:
                res.append(choice.copy())
                return

            for i in range(start_idx, 10):
                if num_len >= k or total_num + i > n:
                    break

                choice.append(i)
                num_len += 1
                total_num += i
                backtrace(i + 1, total_num, num_len, choice)
                choice.pop(-1)
                num_len -= 1
                total_num -= i

        backtrace(1, 0, 0, [])
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.combinationSum3(k=3, n=9)
    print(ret)
