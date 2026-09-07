class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        t = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        return self.solve(text1,text2, n, m,t)
    def solve(self, s1, s2, n, m,t):
        if n == 0 or m == 0:
            return 0
        
        if t[n][m] != -1:
            return t[n][m]

        if s1[n-1] == s2[m-1]:
            t[n][m] =  1 + self.solve(s1,s2,n-1,m-1,t)

        else:
            t[n][m] = max(self.solve(s1,s2, n-1, m,t),self.solve(s1,s2,n,m-1,t))

        return t[n][m]