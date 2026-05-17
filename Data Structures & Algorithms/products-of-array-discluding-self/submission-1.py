class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        out = [1]*len(nums)
        for i in range(1,len(nums)):
            out[i] *= out[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            out[i] *= suffix
            suffix *= nums[i]
        return out

