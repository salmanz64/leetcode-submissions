class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newarr = [0] * (len(nums) *2)
        for i in range(len(nums)):
            newarr[i] = nums[i]
            newarr[len(nums)+i] = nums[i]
        return newarr 
        