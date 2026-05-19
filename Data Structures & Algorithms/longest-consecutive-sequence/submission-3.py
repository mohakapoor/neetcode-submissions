class Solution:
    best = 1
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) 
        best = 0
        for i in nums:
            length = 1
            if not i-1 in nums:
                while i+length in nums:
                    length += 1
            best = max(best,length)
        return best

