class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            print(i,nums[i])
            if nums[i] not in d:
                d[nums[i]] = i
            if target - nums[i] in d and d[target-nums[i]] != i:
                return [d[target-nums[i]],i]

            