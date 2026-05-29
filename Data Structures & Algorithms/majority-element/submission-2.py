
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        for i in nums:
            if nums.count(i) > length/2:
                return i
        