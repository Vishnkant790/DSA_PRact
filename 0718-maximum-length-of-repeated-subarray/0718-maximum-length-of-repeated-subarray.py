class Solution:
    def findLength(self, s1: List[int], s2: List[int]) -> int:
        n = len(s1)
        m = len(s2)
        t = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1): 

                if s1[i-1] != s2[j-1]:
                    continue
                else:
                    t[i][j] =  1 + t[i-1][j-1]
        return max(max(row) for row in t)