class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while left<len(nums)-1:
            while right<len(nums)-1 and nums[right] == 0:
                right += 1
            print(left,right)
            if nums[left] == 0:
                nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right = left +1