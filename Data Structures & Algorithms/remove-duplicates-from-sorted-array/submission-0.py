class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        count = 1
        write = 1
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                nums[write] = nums[right]
                write += 1
                left = right
                count += 1
        return count