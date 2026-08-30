class Solution:
    def lastStoneWeightII(self, arr: List[int]) -> int:
        s = sum(arr)
        n =len(arr)
 
        t = [[False] * (s//2 + 1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0] = True

        for i in range(1,n+1):
            for j in range(1,s//2 + 1):
                
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
                    
                else:
                    t[i][j] = t[i-1][j]
                    
        v = [j for j in range(s//2 + 1) if t[n][j]]
        
        mn = float('inf')
        for i in range(len(v)):
            mn = min(mn, abs(s - 2 * v[i]))
        return mn