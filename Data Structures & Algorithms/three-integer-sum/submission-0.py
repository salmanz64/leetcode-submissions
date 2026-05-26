class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left <right:
                totalSum = nums[i] + nums[left] + nums[right]
                if totalSum < 0:
                    left+=1
                elif totalSum>0:
                    right-=1
                else:
                    op.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return op





        