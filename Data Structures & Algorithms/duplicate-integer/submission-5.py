class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(list(set(nums)))
        return not (len(nums) == len(list(set(nums))))
        