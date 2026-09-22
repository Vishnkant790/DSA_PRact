class Solution:
    def isSubsequence(self, s: str, a: str) -> bool:
        n = len(s)
        m = len(a)
        t = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n +1 ):
            for j in range(1,m+1):
                if s[i-1] == a[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
                
        if t[n][m] == n:
            return True
        else:
            return False