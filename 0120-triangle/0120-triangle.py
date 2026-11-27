class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        dp = [[0]* m for _ in range(m)]
        for j in range(m):
            dp[m-1][j] = triangle[m-1][j]
        for i in range(m-2,-1,-1):
            for j in range(i+1):
                    down = triangle[i][j] + dp[i+1][j]
                    right = triangle[i][j] + dp[i+1][j+1] 
                    dp[i][j] = min(down,right)

        return dp[0][0]


