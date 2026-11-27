class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0:
                    dp[i][j] = grid[0][0]

                else:
                    down = grid[i][j] + (dp[i-1][j] if i > 0 else (float("inf")))
                    right = grid[i][j] + (dp[i][j-1] if j > 0 else (float("inf")))
                    dp[i][j] = min(down,right)

        return dp[m-1][n-1]



