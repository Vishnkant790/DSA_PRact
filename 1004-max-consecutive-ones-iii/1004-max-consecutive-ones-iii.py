class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i = 0
        j = 0
        c = 0
        m = 0
        while j < len(nums):
            if nums[j] == 0:
                m +=1
            while m >k:
                if nums[i] == 0:
                    m-=1
                i+=1
            c = max(c,j-i+1)

            j+=1
        return c 