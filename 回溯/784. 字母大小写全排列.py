from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        length = len(s)

        def backtrace(trace: str, start_idx: int):
            nonlocal length
            if start_idx == length:
                res.append(trace)
                return
            # 首先不管是数字还是字母，都要选择，故进行回溯
            backtrace(trace+s[start_idx], start_idx + 1)
            # 其次如果这个字符是字母的话，相应的另一种状态也要进入回溯
            if s[start_idx].islower():
                backtrace(trace+s[start_idx].upper(), start_idx + 1)
            if s[start_idx].isupper():
                backtrace(trace+s[start_idx].lower(), start_idx + 1)

        backtrace('', 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.letterCasePermutation(s="a1b2")
    print(ret)
