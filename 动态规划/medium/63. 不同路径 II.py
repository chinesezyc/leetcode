from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = obstacleGrid.__len__(), obstacleGrid[0].__len__()
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j]+dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid=[[1]])
    print(result)
