class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        for i in range(1,len(nums)):
            pref[i] *= pref[i-1]*nums[i-1]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            pref[i] *= suffix
            suffix *= nums[i]
        return pref

