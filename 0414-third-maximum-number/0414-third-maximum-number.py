class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Step 1: Duplicates hatao aur descending order mein sort karo
        unique_nums = sorted(set(nums), reverse=True)
        
        # Step 2: Check karo 3rd max exist karta hai kya
        if len(unique_nums) >= 3:
            return unique_nums[2]   # 3rd largest (0-indexed, isliye index 2)
        else:
            return unique_nums[0]   # Sirf maximum return karo