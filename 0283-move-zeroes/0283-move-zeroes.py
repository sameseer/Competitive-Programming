class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in nums:
            if i != 0:
                nums[x] = i
                x += 1
        while x < len(nums):
            nums[x] = 0
            x += 1
            
                