class Solution:
    def jump(self, nums: list[int]) -> int:
        j = 0
        l = 0
        r = 0
        while r < len(nums) -1:
            f = 0
            for i in range(l,r+1):
                f = max(i + nums[i], f)
            l = r+1
            r = f
            j +=1
        return j



