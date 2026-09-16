class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        mid = len(nums) // 2

        if len(nums) <=1:
            return nums

        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left,right)

    def merge(self,left,right)->List[int]:
        i =  j = k = 0
        op = [0] * (len(left) + len(right))
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                op[k] = left[i]
                i+=1
            else:
                op[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            op[k] = left[i]
            k+=1
            i+=1
        while j< len(right):
            op[k] = right[j]
            k+=1
            j+=1

        return op


        


        