class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right and right<len(nums):
                total = nums[i]+nums[left]+nums[right]
                if  total == 0:
                    arr = [nums[i],nums[left],nums[right]]
                    if arr not in out:
                        out.append(arr)
                if total< 0:
                    left += 1
                else:
                    right -= 1
        return out