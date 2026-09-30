class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        dict = {0:1}
        c =0
        ps = 0
        for i in nums:
            ps+=i % 2
            c += dict.get(ps - k, 0)
            dict[ps] = dict.get(ps,0)+1
        return c