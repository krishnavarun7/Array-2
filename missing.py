class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index]>0:
                    nums[index] = -nums[index]
        
        for j in range(len(nums)):
            if nums[j]>0:
                result+= [j+1]
        
        return result