class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for ind in range(l, r + 1):
                farthest = max(farthest, ind + nums[ind])
            l = r + 1
            r = farthest
            jumps += 1
        return jumps