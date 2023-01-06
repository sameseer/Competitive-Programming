class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
            
        ans.extend(nums)
        
        return ans