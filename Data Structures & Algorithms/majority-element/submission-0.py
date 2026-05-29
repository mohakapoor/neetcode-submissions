
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        c = Counter(nums)
        for k,v in c.items():
            if v > length/2:
                return k
        return 1
        