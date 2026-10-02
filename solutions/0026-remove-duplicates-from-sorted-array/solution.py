class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        required_i = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[required_i] = nums[i]
                required_i +=1
        return required_i
        
