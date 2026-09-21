class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        c = 0
        t = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        c+= m - t[n][m]
        c+= n - t[n][m]
        return c
		           
        