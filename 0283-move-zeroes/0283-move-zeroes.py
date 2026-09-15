class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n  = []
        c = 0
        for i in nums:
            if i == 0:
                c+=1
            else:
                n.append(i)
        for i in range(c):
            n.append(0)

        nums[:] = n
        