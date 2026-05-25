class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxCount = 0
        curr = float('-inf')
        for num in setNums:
            if (num -1) not in setNums:
                curr = num
            else:
                curr = float('-inf')
            while curr + 1 in setNums :
                curr = curr+1
            maxCount = max(maxCount,(curr - num)+1)
            
        return maxCount



