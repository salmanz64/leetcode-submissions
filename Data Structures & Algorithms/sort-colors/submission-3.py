class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        curr = 0
        high = len(nums)-1
        while curr < len(nums) and curr <= high:
            print(nums[curr])
            if nums[curr] == 0:
                print('hi')
                nums[low],nums[curr] =nums[curr],nums[low]
                low+=1
                curr+=1
            elif nums[curr] == 2:
                nums[high],nums[curr] =nums[curr],nums[high]
                high-=1
 
            else:
                curr+=1

        
        