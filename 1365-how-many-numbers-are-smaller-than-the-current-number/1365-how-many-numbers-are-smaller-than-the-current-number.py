class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:  
        result = []
        for i in range(len(nums)):
            x = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    x+=1
            result.append(x)
        return result