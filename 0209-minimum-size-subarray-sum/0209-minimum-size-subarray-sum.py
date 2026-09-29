class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        j = 0
        ans = 0
        s = float("inf")
        while j < len(nums):
            ans+=nums[j]
            while ans >=target:
                s = min(s,j-i+1)
                ans -=nums[i]
                    
                i+=1

                
                
            j+=1  

        return s if s != float('inf') else 0           
                    
            