class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d= {}
        for i,n in enumerate(nums):
            val = target -n
            if val in d:
                return [d[val],i]
            d[n] = i
                