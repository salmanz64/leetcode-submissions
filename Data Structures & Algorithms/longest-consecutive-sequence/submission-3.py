class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxCount = 0
        curr = float('-inf')
        for num in setNums:
            if (num - 1) not in setNums:
                curr = num
                count = 1
                while curr + 1 in setNums:
                    curr += 1
                    count += 1
                maxCount = max(maxCount, count)  
        return maxCount



