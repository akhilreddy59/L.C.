class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, mid = 0, 0
        e = len(nums)-1

        while mid <= e:
            if nums[mid] == 0:
                nums[mid], nums[s] = nums[s], nums[mid]
                mid +=1
                s +=1
            elif nums[mid] == 1:
                mid +=1
            else: #nums[mid] == 2:
                nums[mid], nums[e] = nums[e], nums[mid]
                e -=1

        return nums
