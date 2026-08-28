class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        n =len(nums)
        for i in range(n):
            sum += nums[i]
        
        if sum %2 != 0:
            return False
        
        elif sum %2 == 0:
            return self.subset(nums,int (sum/2),n)

    def subset (self, nums, s,n):

        t = [[False]* (s+1) for _ in range(n+1)]

        for i in range(n+1):
            t[i][0] = True

        for i in range(1,n+1):
            for j in range(1,s+1):
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j - nums[i-1]] or t[i-1][j]

                else:
                    t[i][j] = t[i-1][j]

        return t[n][s]

    
