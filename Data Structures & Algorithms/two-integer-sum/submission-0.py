class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                d = {}
                for i in range(0,len(nums)):
                    if d.get(target-nums[i],"no") != "no":
                                return [d[target - nums[i]],i]
                    d[nums[i]] = i            