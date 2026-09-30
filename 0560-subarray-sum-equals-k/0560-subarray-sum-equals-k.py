class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        ps = 0
        c = 0
        for i in nums:
            ps+=i
            c+= seen.get(ps-k,0)
            seen[ps] = seen.get(ps,0) +1
        return c