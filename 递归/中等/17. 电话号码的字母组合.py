from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        info = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = list()
        if digits == '':
            return res

        def findcomb(digits: str, index: int, s: str):
            if index == len(digits):
                res.append(s)
                return
            letters = info[digits[index]]
            for i in range(len(letters)):
                findcomb(digits, index + 1, s + letters[i])
            return

        findcomb(digits, 0, '')
        return res


if __name__ == "__main__":
    solution = Solution()
    ret = solution.letterCombinations(digits="234")
    print(ret)
