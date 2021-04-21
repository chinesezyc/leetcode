from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for h in range(0, 12):
            for m in range(0, 60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    times.append(str(h) + ':' + str(m).zfill(2))
        return times


if __name__ == "__main__":
    solution = Solution()
    ret = solution.readBinaryWatch(turnedOn=1)
    print(ret)
