class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in nums:
            loot = max(
                rob2, # I didnt rob house i
                rob1 + i # I robbed house i therefore rob from 1 before its iteration
                )
            rob1 = rob2
            rob2 = loot
        return loot