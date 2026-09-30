
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        freq = {0:1}
        s = 0
        c = 0
        for x in nums:
            s += x
            c += freq.get(s - goal, 0)
            freq[s] = freq.get(s,0)+1
        return c