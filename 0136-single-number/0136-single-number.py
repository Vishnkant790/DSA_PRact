class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i],0)+1

        for i, v in dict.items():
            if v ==1:
                return i